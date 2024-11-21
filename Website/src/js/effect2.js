document.addEventListener("DOMContentLoaded", () => {
    const rows = document.querySelectorAll("#pointsContainer div");
    rows.forEach((row, index) => {
      row.style.opacity = "0"; // Ensure rows are hidden initially
      row.style.animation = `slideIn 0.5s ease-out forwards`;
      row.style.animationDelay = `${index * 0.2}s`; // Stagger animation by 0.2s for each row
    });
  });

  