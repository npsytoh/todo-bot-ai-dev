const todoCheckboxes = document.querySelectorAll('input[type="checkbox"]');

todoCheckboxes.forEach((checkbox) => {
	checkbox.addEventListener('change', () => {
		const parentElement = checkbox.closest('span');
		const todoTitle = document.getElementById(parentElement.id.replace('checkbox', 'title'));
		todoTitle.classList.toggle('text-decoration-line-through');
	});
});
