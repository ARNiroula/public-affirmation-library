import axios from "axios"


export const registerUser = async (email: string, username: string, password: string) => {
    console.log(email, username, password)
}


export const loginUser = async (username: string, password: string) => {

    try {
        const url_path = `${process.env.NEXT_PUBLIC_API_URL}/api/user/login/`;
        const response = await axios.post(
            url_path,
            { username, password },
            { withCredentials: true }
        );

        return response.data;
    }
    catch (e) {
        throw new Error(`Login Failed => ${e}`)
    }
}
