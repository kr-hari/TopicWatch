import { useState } from 'react';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

function Auth() {
  const [isLogin, setIsLogin] = useState(true); // toggle between login/signup

  return (
    <>
      <Navbar />
      <div className="min-h-[calc(100vh-160px)] flex items-center justify-center bg-gray-100 px-4">
        <div className="bg-white p-8 rounded-xl shadow-lg w-full max-w-md">
          <h2 className="text-3xl font-bold text-center text-indigo-700 mb-2">
            {isLogin ? 'Welcome Back' : 'Join TopicWatch'}
          </h2>
          <p className="text-center text-gray-500 text-sm mb-6">
            {isLogin
              ? 'Access your dashboard and explore what’s trending.'
              : 'Create your account to get started tracking topics.'}
          </p>

          <form className="space-y-4">
            {!isLogin && (
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
                <input
                  type="text"
                  className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
                  placeholder="Jane Doe"
                />
              </div>
            )}

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Email</label>
              <input
                type="email"
                className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
                placeholder="you@example.com"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">Password</label>
              <input
                type="password"
                className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
                placeholder="••••••••"
              />
            </div>

            <button
              type="submit"
              className="w-full bg-indigo-600 text-white py-2 rounded-lg hover:bg-indigo-700 transition"
            >
              {isLogin ? 'Sign In' : 'Sign Up'}
            </button>
          </form>

          {/* Toggle link */}
          <p className="text-sm text-center text-gray-600 mt-4">
            {isLogin ? (
              <>
                Don’t have an account?{' '}
                <button
                  className="text-indigo-600 hover:underline font-medium"
                  onClick={() => setIsLogin(false)}
                >
                  Sign up
                </button>
              </>
            ) : (
              <>
                Already have an account?{' '}
                <button
                  className="text-indigo-600 hover:underline font-medium"
                  onClick={() => setIsLogin(true)}
                >
                  Login
                </button>
              </>
            )}
          </p>

          {/* Google sign in placeholder */}
          <div className="mt-6">
            <div className="relative mb-4">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-gray-300" />
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="bg-white px-2 text-gray-500">or</span>
              </div>
            </div>

            <button className="w-full flex items-center justify-center border rounded-lg py-2 text-gray-600 hover:bg-gray-100">
              <img
                src="https://www.svgrepo.com/show/475656/google-color.svg"
                alt="Google"
                className="w-5 h-5 mr-2"
              />
              Sign in with Google
            </button>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}

export default Auth;


// This code defines an authentication component using React and Tailwind CSS.
// The component allows users to toggle between login and signup forms.
// It includes fields for full name (only in signup), email, and password.
// The form is styled with Tailwind CSS classes for a modern look.
// The component also includes a button to switch between login and signup modes.
// Additionally, there is a placeholder for Google sign-in functionality.
// The component is exported as the default export, making it available for use in other parts of the application.          