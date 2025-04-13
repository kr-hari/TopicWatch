import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="bg-white shadow-md px-6 py-4 flex justify-between items-center">
      <Link to="/" className="text-2xl font-bold text-indigo-700">
        TopicWatch
      </Link>

      <div className="space-x-4">
        <Link to="/" className="text-gray-700 hover:text-indigo-600 font-medium">
          Home
        </Link>
        <Link to="/auth" className="text-gray-700 hover:text-indigo-600 font-medium">
          Login / Signup
        </Link>
      </div>
    </nav>
  );
}

export default Navbar;
//
// This code defines a functional component called Navbar using React.
// The component renders a navigation bar with a logo and links to the home and authentication pages.
// The navigation bar has a white background, shadow effect, and padding.
// It uses Tailwind CSS classes for styling, including flexbox for layout and hover effects for links.
// The logo is a link that redirects to the home page, while the other links navigate to the authentication page.
// The component is designed to be responsive and visually appealing, providing a clean and modern look.
// The Navbar component is exported for use in other parts of the application.
// The use of Tailwind CSS classes allows for easy customization and styling.