function Footer() {
    return (
      <footer className="bg-white text-gray-500 text-sm py-4 mt-10 border-t">
        <div className="max-w-6xl mx-auto px-4 flex justify-between items-center">
          <p>&copy; {new Date().getFullYear()} TopicWatch. All rights reserved.</p>
          <div className="space-x-4">
            <a href="#" className="hover:text-indigo-600">Privacy</a>
            <a href="#" className="hover:text-indigo-600">Terms</a>
            <a href="#" className="hover:text-indigo-600">Contact</a>
          </div>
        </div>
      </footer>
    );
  }
  
  export default Footer;
//
// This code defines a functional component called Footer using React.
// The component renders a footer section with a white background, gray text, and a small font size.                  