import Cookies from "js-cookie";
import { Book } from "@/types/types";

const COOKIE_NAME = "cart";
const COOKIE_PATH = "/";
const COOKIE_EXPIRY_DAYS = 7;

export function getCartFromCookie(): Book[] {
    const cookie = Cookies.get(COOKIE_NAME);
    try {
        return cookie ? JSON.parse(cookie) : [];
    } catch {
        return [];
    }
}

export function saveCartToCookie(cart: Book[]) {
    Cookies.set(COOKIE_NAME, JSON.stringify(cart), {
        expires: COOKIE_EXPIRY_DAYS,
        path: COOKIE_PATH,
    });
}

export function clearCartCookie() {
    Cookies.remove(COOKIE_NAME, { path: COOKIE_PATH });
}

