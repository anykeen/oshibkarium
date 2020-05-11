/**
 * @license Copyright (c) 2003-2019, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function (config) {
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	config.allowedContent =
		'h1 h2 h3 h4 h5 p span blockquote strong em table tbody td tr ul li ol br s strike div form input button label;' +
		'a[href,target];' +
		'td(red,green);' +
		'p(question, sent);' +
		'p[id];' +
		'div(answer);' +
		'button(btn, btn-primary);' +
		'button[id];' +
		'form[id];' +
		'label[*];' +
		'input[*]';
};
