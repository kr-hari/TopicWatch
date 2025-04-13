import { Link } from 'react-router-dom';

function NotFound() {
  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-gray-50 px-4 text-center">
      <h1 className="text-6xl font-bold text-indigo-600 mb-4">404</h1>
      <p className="text-gray-600 text-lg mb-6">
        Oops! The page you’re looking for doesn’t exist.
      </p>
      <Link
        to="/"
        className="px-6 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition"
      >
        Go back home
      </Link>
    </div>
  );
}

export default NotFound;
//
// This code defines a functional component called NotFound using React.
// The component renders a 404 error page with a message indicating that the requested page does not exist.
// It uses Tailwind CSS classes for styling, including a flexbox layout for centering the content.
// The page includes a large "404" heading, a descriptive message, and a button that redirects the user back to the home page.
// The button is styled with a background color, rounded corners, and hover effects.
// The component is designed to provide a user-friendly experience when a page is not found, guiding users back to the main site.