/**
 * @license Copyright (c) 2003-2019, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function (config) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	const domEditableElement = document.querySelector('.ck-editor__editable');
	const editorInstance = domEditableElement.ckeditorInstance;

	editorInstance.editing.view.change(writer => {
		// Map the editable element in the DOM to the editable element in the editor's view.
		const viewEditableRoot = editorInstance.editing.view.domConverter.mapDomToView(domEditableElement);

		writer.setAttribute('class', 'value', viewEditableRoot);
	});
};
