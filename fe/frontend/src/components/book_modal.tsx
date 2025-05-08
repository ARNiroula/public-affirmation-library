import { useEffect, useRef } from 'react';
import { Book } from '@/types/types';

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
            <div ref={ref} className="bg-[#ee917d] p-6 rounded-lg shadow-xl w-96 relative">
                <button onClick={onClose} className="absolute top-2 right-3 text-2xl font-bold text-gray-500 hover:text-black">&times;</button>
                <h2 className="text-xl font-bold mb-2">{book.name}</h2>
                <img src={book.cover_url} alt={book.name} className="w-full h-48 object-contain bg-gray-100 mb-4" />
                <p><strong>ISBN:</strong> {book.isbn}</p>
                <p><strong>Topic:</strong> {book.topic_display}</p>
                <p><strong>Published:</strong> {book.pub_date}</p>
                <p className="mt-2"><strong>Summary:</strong> {book.summary}</p>
            </div>
        </div>
    );
}

