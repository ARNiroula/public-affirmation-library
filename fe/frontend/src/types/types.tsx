export interface BaseAuthorInfo {
    auth_id: number;
    fname: string;
    mname: string | null;
    lname: string | null;
}


export interface Book {
    book_id: number;
    available_copies: number;
    isbn: string;
    name: string;
    topic: string;
    authors: BaseAuthorInfo[] | null;
    topic_display: string;
    summary: string;
    pub_date: string;
    cover_url: string;
}

