import React from 'react';

interface HeaderProps {
  // Add any props you need here
}

const Header: React.FC<HeaderProps> = () => {
  return (
    <header className="bg-gray-900 h-16 flex justify-between items-center">
      <nav className="flex justify-between w-full">
        <ul className="flex justify-between">
          <li className="mr-6">
            <a href="#" className="text-gray-300 hover:text-white">
              Home
            </a>
          </li>
          <li className="mr-6">
            <a href="#" className="text-gray-300 hover:text-white">
              About
            </a>
          </li>
          <li>
            <a href="#" className="text-gray-300 hover:text-white">
              Contact
            </a>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;