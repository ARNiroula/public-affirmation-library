import { useEffect, useRef } from 'react';
import { Book } from '@/types/types';
import Image from 'next/image';

export default function BookModal({ book, onClose }: { book: Book; onClose: () => void }) {
    const ref = useRef<HTMLDivElement>(null);

    useEffect(() => {
        function handleClickOutside(event: MouseEvent) {
            if (ref.current && !ref.current.contains(event.target as Node)) {
                onClose();
            }
        }
        document.addEventListener('mousedown', handleClickOutside);
        return () => document.removeEventListener('mousedown', handleClickOutside);
    }, [ref]);

    return (
        <div className="fixed inset-0 bg-#D2B48C backdrop-blur-sm flex items-center justify-center z-50">
            <div ref={ref} className="bg-purple-900 bg-opacity-1 p-6 rounded-lg shadow-xl w-96 relative">
                <button onClick={onClose} className="absolute top-2 right-3 text-2xl font-bold text-gray-500 hover:text-black">&times;</button>
                <h2 className="text-xl font-bold mb-2">{book.name}</h2>
                <Image
                    src={book.cover_url || "/default.jpg"}
                    width={600}
                    height={400}
                    alt={`Book ${book.name}`}
                    className="w-full h-48 object-contain bg-white transform group-hover:scale-105 transition-transform duration-300"
                />
                <p><strong>ISBN:</strong> {book.isbn}</p>
                <p><strong>Topic:</strong> {book.topic_display}</p>
                <p><strong>Published:</strong> {book.pub_date}</p>
                <p className="mt-2"><strong>Summary:</strong> {book.summary}</p>
                <p className="mt-2"><strong>Authors:</strong> </p>
                {book.authors?.map(author => {
                    return (
                        <p className="mt-2"> {author.fname} {author?.mname} {author?.lname}</p>
                    )
                })}
            </div>
        </div>
    );
}

