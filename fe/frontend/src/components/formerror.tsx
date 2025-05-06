// components/FormError.tsx
type FormErrorProps = {
    message: string;
};

const FormError = ({ message }: FormErrorProps) => {
    if (!message) return null;

    return (
        <div className="text-red-500 bg-red-100 p-2 rounded mb-4">
            {message}
        </div>
    );
};

export default FormError;
