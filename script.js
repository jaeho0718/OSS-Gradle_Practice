function updateTime() {
  const now = new Date();
  document.getElementById('datetime').innerHTML = now.toLocaleString();
}
updateTime();
setInterval(updateTime, 1000);