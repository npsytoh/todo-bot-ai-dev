const todoCheckboxes = document.querySelectorAll('input[type="checkbox"]');

todoCheckboxes.forEach((checkbox) => {
	checkbox.addEventListener('change', () => {
		const todoLabel = document.getElementById(checkbox.id.replace('checkbox', 'label'));
		todoLabel.classList.toggle('text-decoration-line-through');
	});
});
