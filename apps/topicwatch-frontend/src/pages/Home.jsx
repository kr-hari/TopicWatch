import { useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer'; // 👈 import Footer

function Home() {
  const navigate = useNavigate();

  return (
    <>
      <Navbar />
      <div className="min-h-[calc(100vh-160px)] bg-gray-50 flex flex-col items-center justify-center px-4 text-center">
        <h1 className="text-5xl font-extrabold text-indigo-700 mb-4">
          Welcome to <span className="text-indigo-500">TopicWatch</span> 👀
        </h1>
        <p className="text-gray-600 text-lg max-w-2xl mb-8">
          Get real-time insights on emerging tech topics. Stay ahead of the curve by tracking discussions from Reddit communities — summarized and visualized just for you.
        </p>
        <button
          onClick={() => navigate('/auth')}
          className="px-8 py-3 bg-indigo-600 text-white text-lg font-semibold rounded-full hover:bg-indigo-700 transition-all duration-200"
        >
          Get Started
        </button>
      </div>
      <Footer />
    </>
  );
}

export default Home;

//                  