import { useEffect, useState } from "react"

const Index = () => {
  
  useEffect(() => {
    // Define the async function inside the useEffect
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost/api/home');
        const data = await response.json();
        console.log(data); 
      } catch (error) {
        console.error('Error fetching data:', error);
      }
      console.log("hello"); 
    };
  
    fetchData(); 
  }, []);


  return (
    <div>Hello world </div>
  )
}

export default Index