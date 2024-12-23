document.getElementById('edit-btn').addEventListener('click', function() {
    document.getElementById('modal').classList.remove('hidden');
});

document.getElementById('close-modal').addEventListener('click', function() {
    document.getElementById('modal').classList.add('hidden');
});

document.getElementById('profile-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Save new values
    const name = document.getElementById('name').value;
    const bio = document.getElementById('bio').value;

    document.querySelector('.profile-name').textContent = name;
    document.querySelector('.profile-bio').textContent = bio;

    // Close modal
    document.getElementById('modal').classList.add('hidden');
});
