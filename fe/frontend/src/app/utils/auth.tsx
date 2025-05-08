import axios from "axios"

function getCSRFToken(): string | null {
    const matches = document.cookie.match(/csrftoken=([^;]+)/);
    return matches ? matches[1] : null;
}


export type RegisterUserParams = {
    username: string;
    email: string;
    first_name: string;
    last_name: string;
    password: string;
}


export const registerUser = async (
    params: RegisterUserParams
) => {
    try {
        const csrftoken = getCSRFToken();
        const url_path = `${process.env.NEXT_PUBLIC_API_URL}/api/user/register/`;
        const response = await axios.post(
            url_path,
            params,
            {
                withCredentials: true,
                headers: {
                    "X-CSRFToken": csrftoken || "",
                }
            },
        );

        return response.data;
    }
    catch (e) {
        throw new Error(`Register Failed => ${e}`)
    }

}


export const loginUser = async (username: string, password: string) => {

    try {
        const csrftoken = getCSRFToken();
        const url_path = `${process.env.NEXT_PUBLIC_API_URL}/api/user/login/`;
        const response = await axios.post(
            url_path,
            { username, password },
            {
                withCredentials: true,
                headers: {
                    "X-CSRFToken": csrftoken || "",
                }
            },
        );

        return response.data;
    }
    catch (e) {
        throw new Error(`Login Failed => ${e}`)
    }
}


export const logoutUser = async () => {

    try {
        const url_path = `${process.env.NEXT_PUBLIC_API_URL}/api/user/logout/`;
        const response = await axios.post(
            url_path,
            {},
            { withCredentials: true },
        );

        return response.data;
    }
    catch (e) {
        throw new Error(`Logout Failed => ${e}`)
    }
}


export const refreshUser = async () => {

    try {
        const url_path = `${process.env.NEXT_PUBLIC_API_URL}/api/user/refresh/`;
        const response = await axios.post(
            url_path,
            {},
            { withCredentials: true },
        );

        return response.data;
    }
    catch (e) {
        throw new Error(`Refreshing Token Failed Failed => ${e}`)
    }
}
