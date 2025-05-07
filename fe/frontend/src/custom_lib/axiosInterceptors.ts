import api from './axios';

let isRefreshing = false;
let failedQueue: any[] = [];

const processQueue = (error: any, token: string | null = null) => {
    failedQueue.forEach(prom => {
        if (error) {
            prom.reject(error);
        } else {
            prom.resolve(token);
        }
    });

    failedQueue = [];
};

export const setupInterceptors = () => {
    api.interceptors.response.use(
        response => response,
        async error => {
            const originalRequest = error.config;

            if (error.response?.status === 401 && !originalRequest._retry) {
                if (isRefreshing) {
                    return new Promise((resolve, reject) => {
                        failedQueue.push({ resolve, reject });
                    })
                        .then(token => {
                            return api(originalRequest);
                        })
                        .catch(err => {
                            return Promise.reject(err);
                        });
                }

                originalRequest._retry = true;
                isRefreshing = true;

                return new Promise(async (resolve, reject) => {
                    try {
                        await api.post('/user/refresh/');
                        processQueue(null);
                        resolve(api(originalRequest));
                    } catch (err) {
                        processQueue(err, null);
                        reject(err);
                    } finally {
                        isRefreshing = false;
                    }
                });
            }

            return Promise.reject(error);
        }
    );
};

