const onClickToggleButton = (button) => {
	const lastChild = button.lastElementChild;
	const isEnable = lastChild.classList.contains('icon-disable');

	const additionalData = {
		itemState: isEnable,
	};
	const form = button.closest('form');
	postFormData(form, additionalData);

	lastChild.classList.toggle('icon-disable');
	lastChild.classList.toggle('icon-enable');

	const itemTitle = button.closest('td').nextElementSibling;
	itemTitle.classList.toggle('text-decoration-line-through');
};

const postFormData = (form, data) => {
	const formData = new FormData(form);

	for (const key in data) {
		if (data.hasOwnProperty(key)) {
			formData.append(key, data[key]);
		}
	}

	const action = form.getAttribute('action');
	const options = {
		method: 'POST',
		body: formData,
	};
	fetch(action, options).then((e) => {
		if (e.status === 200) {
			console.log('[' + Date(Date.now()) + '] POST success.');
			return;
		}
		console.log('[' + Date(Date.now()) + '] POST failed.');
	});
};

const itemButtons = document.querySelectorAll('.button-toggle');

itemButtons.forEach((button) => {
	button.addEventListener('click', () => {
		onClickToggleButton(button);
	});
});
