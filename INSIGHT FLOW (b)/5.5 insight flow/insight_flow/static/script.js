// script.js - 사이드바 토글 등 JS
document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("toggle-btn");
    const sidebar = document.getElementById("sidebar");
  
    toggleBtn.addEventListener("click", function () {
      sidebar.classList.toggle("closed");
    });
  });
  