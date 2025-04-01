document.getElementById('fbForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    document.getElementById('status').textContent = "Processing...";

    const data = {
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
        firstname: document.getElementById('firstname').value,
        lastname: document.getElementById('lastname').value,
        dob: document.getElementById('dob').value
    };

    const response = await fetch('https://your-app-name.onrender.com/create_fb_account', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    document.getElementById('status').textContent = result.message;
});
