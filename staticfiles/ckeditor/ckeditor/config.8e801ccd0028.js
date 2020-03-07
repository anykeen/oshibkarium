/**
 * @license Copyright (c) 2003-2019, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function (config) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	editor.editing.view.change( writer => {
		const viewEditableRoot = editor.editing.view.document.getRoot();
	
		writer.setAttribute( 'class', 'value', viewEditableRoot );
	} );
};
