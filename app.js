document.getElementById("check-health").addEventListener("click", async () => {
    const resultEl = document.getElementById("health-result");
    resultEl.textContent = "Checking...";
    try {
        const res = await fetch("/api/health");
        const data = await res.json();
        resultEl.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        resultEl.textContent = `Error: ${err.message}`;
    }
});
