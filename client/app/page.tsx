"use client";
import { useEffect, useState } from "react";

function Index() {
  const [message, setMessage] = useState("Loading");
  const [people, setPeople] = useState([]);
  const [randomNum, setRandomNum] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8080/api/home");
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        setMessage(data.message);
        setPeople(data.people);
        setRandomNum(data.randomNum);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <>
      <div>{message}</div>
      <div>Random Number is: {randomNum}</div>
      {people.map((person, index) => (
        <div key={index}>My name is: {person}</div>
      ))}
    </>
  );
}

export default Index;
