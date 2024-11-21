document.addEventListener('DOMContentLoaded', () => {
    const welcomeText = document.getElementById('welcomeText');
    const text = "Welcome!";
    let index = 0;
  
    function typeLetterByLetter() {
      if (index < text.length) {
        welcomeText.textContent += text[index];
        index++;
        setTimeout(typeLetterByLetter, 200); // Delay between letters
      } else {
        setTimeout(() => {
          welcomeText.textContent = ''; // Clear content before restarting
          index = 0;
          typeLetterByLetter(); // Restart the typing effect
        }, 1000); // Delay before restarting
      }
    }
  
    typeLetterByLetter();
  });
  