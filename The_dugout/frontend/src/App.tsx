import React, { useState } from 'react';
import { Newspaper, Users, BookOpen, Home, ExternalLink } from 'lucide-react';

function App() {
  const [activeTab, setActiveTab] = useState('home');

  const news = [
    {
      title: "Mbappé's Future: Real Madrid Transfer Saga Continues",
      image: "https://images.unsplash.com/photo-1489944440615-453fc2b6a9a9?auto=format&fit=crop&q=80&w=800",
      summary: "Latest updates on the potential transfer of Kylian Mbappé to Real Madrid..."
    },
    {
      title: "Premier League Transfer Window Updates",
      image: "https://images.unsplash.com/photo-1522778119026-d647f0596c20?auto=format&fit=crop&q=80&w=800",
      summary: "Top clubs looking to strengthen their squads ahead of the upcoming season..."
    }
  ];

  const tactics = [
    {
      title: "Modern Pressing Tactics in Football",
      image: "https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?auto=format&fit=crop&q=80&w=800",
      summary: "An analysis of high-pressing tactics in modern football..."
    },
    {
      title: "The Evolution of the False 9",
      image: "https://images.unsplash.com/photo-1517466787929-bc90951d0974?auto=format&fit=crop&q=80&w=800",
      summary: "Understanding the role and impact of the false 9 position..."
    }
  ];

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Navigation Bar */}
      <nav className="bg-blue-600 text-white shadow-lg">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center space-x-4">
              <Home className="w-6 h-6" />
              <span className="font-bold text-xl">Tunnel Vision</span>
            </div>
            <div className="flex space-x-4">
              <button
                onClick={() => setActiveTab('home')}
                className={`px-3 py-2 rounded-md ${activeTab === 'home' ? 'bg-blue-700' : 'hover:bg-blue-700'}`}
              >
                Home
              </button>
              <button
                onClick={() => setActiveTab('news')}
                className={`px-3 py-2 rounded-md ${activeTab === 'news' ? 'bg-blue-700' : 'hover:bg-blue-700'}`}
              >
                News
              </button>
              <button
                onClick={() => setActiveTab('tactics')}
                className={`px-3 py-2 rounded-md ${activeTab === 'tactics' ? 'bg-blue-700' : 'hover:bg-blue-700'}`}
              >
                Tactics
              </button>
              <button
                onClick={() => setActiveTab('about')}
                className={`px-3 py-2 rounded-md ${activeTab === 'about' ? 'bg-blue-700' : 'hover:bg-blue-700'}`}
              >
                About
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 py-8">
        {activeTab === 'home' && (
          <div className="space-y-8">
            <section className="relative h-96 rounded-xl overflow-hidden">
              <img
                src="https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&q=80&w=1200"
                alt="Soccer stadium"
                className="w-full h-full object-cover"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent flex items-end">
                <div className="p-8 text-white">
                  <h1 className="text-4xl font-bold mb-2">Welcome to Soccer Hub</h1>
                  <p className="text-xl">Your source for the latest soccer news, tactics, and analysis</p>
                </div>
              </div>
            </section>

            <div className="grid md:grid-cols-2 gap-8">
              <section>
                <h2 className="text-2xl font-bold mb-4 flex items-center">
                  <Newspaper className="w-6 h-6 mr-2" />
                  Latest News
                </h2>
                <div className="space-y-4">
                  {news.map((item, index) => (
                    <div key={index} className="bg-white rounded-lg shadow-md overflow-hidden">
                      <img src={item.image} alt={item.title} className="w-full h-48 object-cover" />
                      <div className="p-4">
                        <h3 className="font-bold text-lg mb-2">{item.title}</h3>
                        <p className="text-gray-600">{item.summary}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </section>

              <section>
                <h2 className="text-2xl font-bold mb-4 flex items-center">
                  <BookOpen className="w-6 h-6 mr-2" />
                  Latest Tactics
                </h2>
                <div className="space-y-4">
                  {tactics.map((item, index) => (
                    <div key={index} className="bg-white rounded-lg shadow-md overflow-hidden">
                      <img src={item.image} alt={item.title} className="w-full h-48 object-cover" />
                      <div className="p-4">
                        <h3 className="font-bold text-lg mb-2">{item.title}</h3>
                        <p className="text-gray-600">{item.summary}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </section>
            </div>
          </div>
        )}

        {activeTab === 'about' && (
          <div className="bg-white rounded-lg shadow-md p-8">
            <h2 className="text-2xl font-bold mb-4 flex items-center">
              <Users className="w-6 h-6 mr-2" />
              About the Creator
            </h2>
            <div className="prose max-w-none">
              <p className="text-gray-600">
                Soccer Hub was created by passionate soccer enthusiasts who wanted to bring the latest news,
                tactical analysis, and insights to football fans worldwide. Our team consists of experienced
                sports journalists, former players, and tactical analysts who work together to provide
                high-quality content for our readers.
              </p>
            </div>
          </div>
        )}

        {/* External Links */}
        <div className="mt-8 bg-white rounded-lg shadow-md p-6">
          <h2 className="text-xl font-bold mb-4 flex items-center">
            <ExternalLink className="w-6 h-6 mr-2" />
            Quick Links
          </h2>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <a href="#" className="text-blue-600 hover:text-blue-800 flex items-center">
              <span className="mr-2">⚽</span> Live Scores
            </a>
            <a href="#" className="text-blue-600 hover:text-blue-800 flex items-center">
              <span className="mr-2">📊</span> Statistics
            </a>
            <a href="#" className="text-blue-600 hover:text-blue-800 flex items-center">
              <span className="mr-2">🎮</span> Fantasy League
            </a>
            <a href="#" className="text-blue-600 hover:text-blue-800 flex items-center">
              <span className="mr-2">📱</span> Mobile App
            </a>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-800 text-white mt-12">
        <div className="max-w-7xl mx-auto px-4 py-8">
          <div className="text-center">
            <p>© 2024 Soccer Hub. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;