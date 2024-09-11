const itemButtons = document.querySelectorAll('.button-toggle');

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
			console.log('[' + Date(Date.now()) + '] post success.');
			return;
		}
		console.log('[' + Date(Date.now()) + '] post failed.');
	});
};

itemButtons.forEach((button) => {
	button.addEventListener('click', () => {
		const lastChild = button.lastElementChild;
		const isDisable = lastChild.classList.contains('icon-disable');

		if (isDisable) {
			console.log('完了しました');
		} else {
			console.log('完了キャンセル');
		}

		const additionalData = {
			itemStatus: isDisable,
		};
		const form = button.closest('form');
		postFormData(form, additionalData);

		lastChild.classList.toggle('icon-disable');
		lastChild.classList.toggle('icon-enable');
	});
});
