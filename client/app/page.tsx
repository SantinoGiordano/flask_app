'use client';
import { useEffect, useState } from 'react';

function Index(){

  const[message, setMessage] = useState('')

  useEffect(() => {
    const fetchData = async () => {
      try {
        console.log('Fetching data...');
        const response = await fetch('http://localhost:8080/api/home');
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Fetched data:', data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData(); 
  }, []);

  return (
    <div>Hello world </div>
  );
}

export default Index;
