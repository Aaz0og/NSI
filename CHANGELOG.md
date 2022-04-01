# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [2.21.1](https://github.com/filebrowser/filebrowser/compare/v2.21.0...v2.21.1) (2022-02-22)


### Bug Fixes

* display user scope for admin users ([#1834](https://github.com/filebrowser/filebrowser/issues/1834)) ([6366cf0](https://github.com/filebrowser/filebrowser/commit/6366cf0b181f13eac38f69f1760d6f6f0586a5d1))

## [2.21.0](https://github.com/filebrowser/filebrowser/compare/v2.20.1...v2.21.0) (2022-02-21)


### Features

* add colorized file type icons ([2948589](https://github.com/filebrowser/filebrowser/commit/2948589fcde6d1dca7f3ea52a621d8213fa3300c))
* add gallery view mode ([8888b9f](https://github.com/filebrowser/filebrowser/commit/8888b9f44640394df9e3583db4392472d7027a4b))
* add Ukrainian translation / update Russian translation ([#1753](https://github.com/filebrowser/filebrowser/issues/1753)) ([665e458](https://github.com/filebrowser/filebrowser/commit/665e45889cd333f1e3500e4bf38d15d229c9fe2a))
* add upload file list with progress ([#1825](https://github.com/filebrowser/filebrowser/issues/1825)) ([cf85404](https://github.com/filebrowser/filebrowser/commit/cf85404dd25cd7fdd73aa32878b4dc5f85ee3e96))
* smaller column width to fit 2 columns in landscape mobiles ([7870e89](https://github.com/filebrowser/filebrowser/commit/7870e89bc04f1494f2705795476b5f1c9d621e38))
* use real image path to calculate cache key ([c198723](https://github.com/filebrowser/filebrowser/commit/c1987237d05adcce77c614e5247a181ae5cdfacd))


### Bug Fixes

* correctly handle non-ascii passwords for shared resources ([c782f21](https://github.com/filebrowser/filebrowser/commit/c782f21b0fa4511a15e7015117d075eaf5ea332c))
* don't expose scope for non-admin users ([0942fc7](https://github.com/filebrowser/filebrowser/commit/0942fc7042fd949cce91855169d0bcf16eb75771))
* open all the pdf files correctly ([#1742](https://github.com/filebrowser/filebrowser/issues/1742)) ([949f0f2](https://github.com/filebrowser/filebrowser/commit/949f0f277f6004904b3edfa716a8365ec93fa0fa))


### Build

* **deps:** bump browserslist from 4.16.3 to 4.19.1 in /frontend ([8089007](https://github.com/filebrowser/filebrowser/commit/80890075e802e2a4217edbb01d6417122d702f5e))
* **deps:** bump dns-packet from 1.3.1 to 1.3.4 in /frontend ([a73d7f1](https://github.com/filebrowser/filebrowser/commit/a73d7f14b787935c6ebe525dba64b65f8ed733e2))
* **deps:** bump follow-redirects from 1.13.3 to 1.14.8 in /frontend ([f1f7f17](https://github.com/filebrowser/filebrowser/commit/f1f7f17ade8d40fc6cfb22c79960bce299876b56))
* **deps:** bump hosted-git-info from 2.8.8 to 2.8.9 in /frontend ([e7659ea](https://github.com/filebrowser/filebrowser/commit/e7659ea36bdf780ce17005f7170a2fef02a2d5e5))
* **deps:** bump path-parse from 1.0.6 to 1.0.7 in /frontend ([c014966](https://github.com/filebrowser/filebrowser/commit/c01496624a7ebfc8a7c256bd919a400367281cbb))
* **deps:** bump postcss from 7.0.35 to 7.0.39 in /frontend ([9182d33](https://github.com/filebrowser/filebrowser/commit/9182d33e1cc375473fb18989a92d20252884f096))
* **deps:** bump ssri from 6.0.1 to 6.0.2 in /frontend ([3717186](https://github.com/filebrowser/filebrowser/commit/371718634b11f32e68165f31c51b6b1139c829ec))
* **deps:** bump tar from 6.1.0 to 6.1.11 in /frontend ([010d16f](https://github.com/filebrowser/filebrowser/commit/010d16fc1d8f0200e5662943aef17ee89c5877b7))
* **deps:** bump url-parse from 1.5.1 to 1.5.4 in /frontend ([8906408](https://github.com/filebrowser/filebrowser/commit/8906408a8f0ed86d1e11ea90fc573b36815c9c0d))
* **deps:** bump url-parse from 1.5.4 to 1.5.7 in /frontend ([228ebea](https://github.com/filebrowser/filebrowser/commit/228ebea66cc871b33459406590a80ef906298e7d))
* **deps:** bump ws from 6.2.1 to 6.2.2 in /frontend ([73c8073](https://github.com/filebrowser/filebrowser/commit/73c80732d934bc8802a6d7c7a559cad37df405f0))

### [2.20.1](https://github.com/filebrowser/filebrowser/compare/v2.20.0...v2.20.1) (2021-12-21)


### Build

* revert to using the default alpine based docker image ([46d8046](https://github.com/filebrowser/filebrowser/commit/46d80464d2a67927b06a11b83fb137ad364a90ed))

## [2.20.0](https://github.com/filebrowser/filebrowser/compare/v2.19.0...v2.20.0) (2021-12-20)


### Features

* detect multiple subtitle languages ([#1723](https://github.com/filebrowser/filebrowser/issues/1723)) ([c2e03bb](https://github.com/filebrowser/filebrowser/commit/c2e03bbfab97fc6716bcdd59158e9d5129bf0ea7))
* use linuxserver based docker image ([b8f35ce](https://github.com/filebrowser/filebrowser/commit/b8f35ce9322c2b0dbf954cfd3ff584bc9f742fdd))


### Bug Fixes

* set correct default database path in the config ([988d3e5](https://github.com/filebrowser/filebrowser/commit/988d3e5bdd224509ddc2f08444560e3087e9c67d))
* upgrade vulnerable versions of the library ([6eb3ab0](https://github.com/filebrowser/filebrowser/commit/6eb3ab063509a015ad630ab704ae3791461d0982))


### Build

* refactor makefile ([f81857a](https://github.com/filebrowser/filebrowser/commit/f81857acce25936a700945db5ef4af545eaeb1cf))
* remove deprecated goreleaser use_buildx param ([4d1b9dd](https://github.com/filebrowser/filebrowser/commit/4d1b9dd2112002a93bb26cece07dcfd81c31dc2c))

## [2.19.0](https://github.com/filebrowser/filebrowser/compare/v2.18.0...v2.19.0) (2021-11-24)


### Features

* prefetch previous and next images in preview. ([#1627](https://github.com/filebrowser/filebrowser/issues/1627)) ([7401d16](https://github.com/filebrowser/filebrowser/commit/7401d16e457bb232fd7dd7ef427e8960d465705c))


### Bug Fixes

* empty file listing on share ([e082397](https://github.com/filebrowser/filebrowser/commit/e08239781f61e7bb25d9b8c5c6cce90f34621a76))
* relative font sizes ([c29698d](https://github.com/filebrowser/filebrowser/commit/c29698dffac769077ab7c7869569a902979ee3d7))

## [2.18.0](https://github.com/filebrowser/filebrowser/compare/v2.17.2...v2.18.0) (2021-10-31)


### Features

* add ability to select file modified time format ([#1536](https://github.com/filebrowser/filebrowser/issues/1536)) ([0426629](https://github.com/filebrowser/filebrowser/commit/0426629a59c712849570d3e29956948ae7725a4a))
* add manifest theme color param ([#1542](https://github.com/filebrowser/filebrowser/issues/1542)) ([0358e42](https://github.com/filebrowser/filebrowser/commit/0358e42d2c206732fffa77714f5a66f4fe50a69d))


### Bug Fixes

* back button behaviour in preview ([#1573](https://github.com/filebrowser/filebrowser/issues/1573)) ([deabc80](https://github.com/filebrowser/filebrowser/commit/deabc80fd7670983039dfcd29531b45002ca5d9e))
* fix sidebar navigation on mobile devices ([#1618](https://github.com/filebrowser/filebrowser/issues/1618)) ([f09bf3e](https://github.com/filebrowser/filebrowser/commit/f09bf3e1d076b27d29ba8a91cf448a99993bc444))
* search box is misaligned when the browser preferred font size is other than 16px ([#1613](https://github.com/filebrowser/filebrowser/issues/1613)) ([6f345be](https://github.com/filebrowser/filebrowser/commit/6f345be3e47ba57ecc1eb9a62587ab949078c125))
* security issue in command runner (closes [#1621](https://github.com/filebrowser/filebrowser/issues/1621)) ([74b7cd8](https://github.com/filebrowser/filebrowser/commit/74b7cd8e81840537a8206317344f118093153e8d))
* set correct editor height regardless of preferred font size ([#1614](https://github.com/filebrowser/filebrowser/issues/1614)) ([ddd4ffa](https://github.com/filebrowser/filebrowser/commit/ddd4ffa4caa6b292a3a644ecd897aba1237c7503))
* zoom pics when dlclick at first time ([#1561](https://github.com/filebrowser/filebrowser/issues/1561)) ([b6a51be](https://github.com/filebrowser/filebrowser/commit/b6a51bed516814944f8aa41440652242d57824c5))

### [2.17.2](https://github.com/filebrowser/filebrowser/compare/v2.17.1...v2.17.2) (2021-08-27)


### Bug Fixes

* bug with inlineLink not creating url properly ([#1515](https://github.com/filebrowser/filebrowser/issues/1515)) ([43a4609](https://github.com/filebrowser/filebrowser/commit/43a460993c3f0d158b876db4b20caa7963e9f361))

### [2.17.1](https://github.com/filebrowser/filebrowser/compare/v2.17.0...v2.17.1) (2021-08-23)


### Bug Fixes

* internal server error if --disable-preview-resize flag is set (closes [#1510](https://github.com/filebrowser/filebrowser/issues/1510)) ([4c3099a](https://github.com/filebrowser/filebrowser/commit/4c3099a086c206dcb3bc70ee8c8da02eee61c30b))

## [2.17.0](https://github.com/filebrowser/filebrowser/compare/v2.16.1...v2.17.0) (2021-08-21)


### Features

* open file option on preview ([76add9e](https://github.com/filebrowser/filebrowser/commit/76add9e5274b0373c6b983e3b20e387a14ea6c9e))


### Bug Fixes

* 401 error in share view open file button ([#1495](https://github.com/filebrowser/filebrowser/issues/1495)) ([25c8788](https://github.com/filebrowser/filebrowser/commit/25c87883908babde073390a2e2320a8e5880a87c))
* escape quote on index template ([23d646c](https://github.com/filebrowser/filebrowser/commit/23d646c456876d06cf48e71c1e57b69de99511f0)), closes [#1501](https://github.com/filebrowser/filebrowser/issues/1501)
* file caching directive ([c63cc5a](https://github.com/filebrowser/filebrowser/commit/c63cc5a2d25909cc4e2f2e7235f276ec66c32bf2))

### [2.16.1](https://github.com/filebrowser/filebrowser/compare/v2.16.0...v2.16.1) (2021-08-04)


### Bug Fixes

* check symlink target type (closes [#1488](https://github.com/filebrowser/filebrowser/issues/1488)) ([76b466f](https://github.com/filebrowser/filebrowser/commit/76b466f6492e74cf13e66a33e7e5f597ac92b240))

## [2.16.0](https://github.com/filebrowser/filebrowser/compare/v2.15.0...v2.16.0) (2021-07-26)


### Features

* browser cache directives ([190cb99](https://github.com/filebrowser/filebrowser/commit/190cb99a79a0d438eca2da13539f8c6449ad73ac))
* display error messages on settings ([6032038](https://github.com/filebrowser/filebrowser/commit/603203848a8b2221158088b6d849609db4c0c46c))
* file name on page title ([16a34de](https://github.com/filebrowser/filebrowser/commit/16a34defc02554a77c6ac47b9e17e69d098a09fe))
* gzip encoding for static js files ([aa172b8](https://github.com/filebrowser/filebrowser/commit/aa172b8bb5f17d5f5cb9666bfb5ee650d8091fb5))
* loading spinner on views navigation ([976eb55](https://github.com/filebrowser/filebrowser/commit/976eb5583dae474125fd7ddec5dc19b6c291f98f))
* message for connection error ([5e6f14b](https://github.com/filebrowser/filebrowser/commit/5e6f14b5dcb9c5efdf526f1346e09c2d0b2f6974))
* mod time title on file info ([7d1e030](https://github.com/filebrowser/filebrowser/commit/7d1e03075d2c27148f60813defa0f68403d1d3c2))
* open file option on share ([1c25f6e](https://github.com/filebrowser/filebrowser/commit/1c25f6ee69bd71eed82af7020006d0e27537a967))
* show more button on share ([ba8c09f](https://github.com/filebrowser/filebrowser/commit/ba8c09f454feeadf4a1e97547a34151a81b389d5))
* support for IE11 browser ([7ec24d9](https://github.com/filebrowser/filebrowser/commit/7ec24d9d7794fa37825f64ca2d1575f568fb1362))


### Bug Fixes

* break resource create/update handlers on error (closes [#1464](https://github.com/filebrowser/filebrowser/issues/1464)) ([5072bbb](https://github.com/filebrowser/filebrowser/commit/5072bbb2cbf5b29d041629faa8367f15e4d145a2))
* copying files with special characters ([20ebbf6](https://github.com/filebrowser/filebrowser/commit/20ebbf6611b734371426fb1b9cb5e388be90bf7e))
* delete image cache when moving ([8973c45](https://github.com/filebrowser/filebrowser/commit/8973c4598ff817647f1f1ad6ee36480054cd2776))
* don't remove files on unsuccessful updates (closes [#1456](https://github.com/filebrowser/filebrowser/issues/1456)) ([6b19ab6](https://github.com/filebrowser/filebrowser/commit/6b19ab6613b12be7f075299cd98f4b41d43827c7))
* failure on broken symlink deletion ([8650d2f](https://github.com/filebrowser/filebrowser/commit/8650d2ffe7a29cbafa800efcecbf6a61598a9f0c))
* inconsistent double click on listing item ([ba7e71a](https://github.com/filebrowser/filebrowser/commit/ba7e71a7c3b0cc71012e5adf94b1c642e554972e))
* no items displayed on file listing ([18889ad](https://github.com/filebrowser/filebrowser/commit/18889ad725f7f7e5a7e3f7abcf156487556dbeaf))
* omit file content ([209f9fa](https://github.com/filebrowser/filebrowser/commit/209f9fa77f751054512355f2b74b9b7258465d0b))
* short commit sha and typo fix in Makefile ([#1411](https://github.com/filebrowser/filebrowser/issues/1411)) ([46ee595](https://github.com/filebrowser/filebrowser/commit/46ee59538914dc2859f0da6b32e2d062d0a01b10))

## [2.15.0](https://github.com/filebrowser/filebrowser/compare/v2.14.1...v2.15.0) (2021-04-06)


### Features

* add EXIF thumbnail support for JPEG files ([#1234](https://github.com/filebrowser/filebrowser/issues/1234)) ([7dd5b34](https://github.com/filebrowser/filebrowser/commit/7dd5b34d425dfbc2782152310483cbecf85c800a))
* dynamic autoplay on previewer ([a76e01d](https://github.com/filebrowser/filebrowser/commit/a76e01d2b78a785f3665a8b3532c7cc566bfabce))
* dynamic item count on file listing ([6c8ee96](https://github.com/filebrowser/filebrowser/commit/6c8ee96e6a21fae5d4608bdc7a5c5a161d7dafd3))
* dynamic zoom limit on previewer ([e410272](https://github.com/filebrowser/filebrowser/commit/e410272e6be6a0b660efe8d4eee6c6e9dd834cc5))


### Bug Fixes

* buttons without permission on header ([1516d99](https://github.com/filebrowser/filebrowser/commit/1516d9932bf9926ac8b4cb3e738a5f51e80d5b1d))
* check modify permission on file overwrite ([59f9964](https://github.com/filebrowser/filebrowser/commit/59f9964e80c8233775f27be33a4c16a31bfe848a))
* empty archive name on directory download ([2697093](https://github.com/filebrowser/filebrowser/commit/2697093ac151f74eea3022951d128acfe04d1dcf))
* empty text file on editor ([e9baf0c](https://github.com/filebrowser/filebrowser/commit/e9baf0c4b688fab291cdc842ec464c7a7a816499))
* error causes panic on upload ([e1a6f59](https://github.com/filebrowser/filebrowser/commit/e1a6f593e1824e7fa4345a61dff5b1bb8cd22d05))
* hidden editor header on Safari ([b521dec](https://github.com/filebrowser/filebrowser/commit/b521dec8f9b14dd92248c429e902ebc639046389))
* image quality switch on previewer ([c0d85f3](https://github.com/filebrowser/filebrowser/commit/c0d85f3d85926c8790757bf142140d19455ae8ca))
* list item interactions on share ([87f1881](https://github.com/filebrowser/filebrowser/commit/87f1881b429877a740ea84a8e783ad4103248289))
* missing bold variation for Roboto font ([98d79b8](https://github.com/filebrowser/filebrowser/commit/98d79b8ed955df5691a306d709b4ab60d91da408))
* mouse wheel zoom on previewer ([fcb115f](https://github.com/filebrowser/filebrowser/commit/fcb115f42d33db2be7a4d428ec53d65d6050320b))
* no header button animations on file listing ([fe80730](https://github.com/filebrowser/filebrowser/commit/fe80730bb135b38e4d9de470c75cbe10b1aec201))

### [2.14.1](https://github.com/filebrowser/filebrowser/compare/v2.14.0...v2.14.1) (2021-03-21)


### Bug Fixes

* display public routes with header proxy auth ([da54bd6](https://github.com/filebrowser/filebrowser/commit/da54bd6c214d7ee39b71d710ddfe6dd25fc4e5d6))

## [2.14.0](https://github.com/filebrowser/filebrowser/compare/v2.13.0...v2.14.0) (2021-03-21)


### Features

* add health check handler ([a721dc1](https://github.com/filebrowser/filebrowser/commit/a721dc1f314732e60d331a1a7da97d06e0e8b613))


### Bug Fixes

* hide dotfile error on share ([5f4a031](https://github.com/filebrowser/filebrowser/commit/5f4a0317ab5685fe4a558df74e604c12e04a1c10))
* prefix handling on http router ([93a35ad](https://github.com/filebrowser/filebrowser/commit/93a35ad2516accdcb9735db509550979d01de2c3))
* qr code url on share ([22f4be8](https://github.com/filebrowser/filebrowser/commit/22f4be8f54162b7cf494177705ffb8b09117bd01))
* text file detection on editor ([eeadc53](https://github.com/filebrowser/filebrowser/commit/eeadc532fe6057969b3c1a4726f236851b154cfa))

## [2.13.0](https://github.com/filebrowser/filebrowser/compare/v2.12.1...v2.13.0) (2021-03-14)


### Features

* dual pane settings view ([db5aad8](https://github.com/filebrowser/filebrowser/commit/db5aad8eb679cfe1b1ace5142cf342951217f0f7))
* improved settings navbar ([5b28aa0](https://github.com/filebrowser/filebrowser/commit/5b28aa0848710b9d3ee02a2aa912856395f48bd2))
* improved sharing prompt ([1819377](https://github.com/filebrowser/filebrowser/commit/18193778971e27d18b5a35df8c2d0e2953b48111))
* increased header button counter size ([4fb832c](https://github.com/filebrowser/filebrowser/commit/4fb832c0422107e16f22b7aa928224f36de4978f))
* larger previewer content ([62fff5c](https://github.com/filebrowser/filebrowser/commit/62fff5ca60da1f887c1f95fa4808d3753596dab2))


### Bug Fixes

* archive contains parent path on Windows ([54f3570](https://github.com/filebrowser/filebrowser/commit/54f35701a2bd5cb7ec0628ca9789047072c073db))
* check rules on http resource handlers ([5bf1554](https://github.com/filebrowser/filebrowser/commit/5bf15548d0ad147acfad5000277531be2671f7ce))
* download current dir on file listing ([488d980](https://github.com/filebrowser/filebrowser/commit/488d98045e7476ed11e53c13d9498a9db3165bbc))
* encoded file path on share ([7955e07](https://github.com/filebrowser/filebrowser/commit/7955e0720baef3710106c7e69bbbf078d5489220))
* full file path on share ([e017a19](https://github.com/filebrowser/filebrowser/commit/e017a199850e19dd51b960ba59402c215fd8f1af))
* header dropdown icon color on previewer ([f8df76f](https://github.com/filebrowser/filebrowser/commit/f8df76f52684f10722ce123fec2c90e321ddf103))
* item dragging on file listing ([326b35a](https://github.com/filebrowser/filebrowser/commit/326b35a7ac7871afcdf892ca150349665b7f6379))
* modified time on info prompt ([11ebaec](https://github.com/filebrowser/filebrowser/commit/11ebaec5f0671ec02ebe55d4a73a514bce3a6713))
* root path name on archive ([426b38b](https://github.com/filebrowser/filebrowser/commit/426b38bb3362d2d477d0d8aa27d880664d537431))
* stuck icon on header button ([6a734c0](https://github.com/filebrowser/filebrowser/commit/6a734c01391b437c2842f5d97fb63f29a0017510))
* update image cache when replacing ([81b6f4d](https://github.com/filebrowser/filebrowser/commit/81b6f4d6f6a01886583016f61f4f1951a59f244d))
* wait for async command exit ([#1326](https://github.com/filebrowser/filebrowser/issues/1326)) ([6d5ceae](https://github.com/filebrowser/filebrowser/commit/6d5ceae8b454edd749b3b65c88aacc0a31ce9215))


### Refactorings

* migrate from rice to embed.FS ([fc55061](https://github.com/filebrowser/filebrowser/commit/fc5506179a64e9e2f57f7b6d6cce4b95f5ebc235))

### [2.12.1](https://github.com/filebrowser/filebrowser/compare/v2.12.0...v2.12.1) (2021-03-07)


### Bug Fixes

* add missing default config into the docker image ([7358b3f](https://github.com/filebrowser/filebrowser/commit/7358b3fe3178c20007b4b5ef5c03705badd538c4))

## [2.12.0](https://github.com/filebrowser/filebrowser/compare/v2.11.0...v2.12.0) (2021-03-04)


### Features

* add homebrew tap ([2d2c598](https://github.com/filebrowser/filebrowser/commit/2d2c598fa6bd1ecaf39c542182890c8dd9b1cad0))
* added tiff files preview support ([#1222](https://github.com/filebrowser/filebrowser/issues/1222)) ([e8c9d1c](https://github.com/filebrowser/filebrowser/commit/e8c9d1c53989b4b52f6fba2a8ac41ae612c03a7c))
* allow disabling file detections by reading header ([#1175](https://github.com/filebrowser/filebrowser/issues/1175)) ([6914063](https://github.com/filebrowser/filebrowser/commit/6914063853a8a3f3cecfa4b21f223820c2a0b7df))
* allow to password protect shares ([#1252](https://github.com/filebrowser/filebrowser/issues/1252)) ([d8f415f](https://github.com/filebrowser/filebrowser/commit/d8f415f8abd0c4301803bd968c54429dd3fe4b59))
* build multi-arch docker images ([cf4836d](https://github.com/filebrowser/filebrowser/commit/cf4836dc757ef79ad615179bb7a6c7bbd3b09c2c))
* share management delete confirm ([#1212](https://github.com/filebrowser/filebrowser/issues/1212)) ([b600b11](https://github.com/filebrowser/filebrowser/commit/b600b11415fd1fb90ff2f5136be95a9c737ae1cb))


### Bug Fixes

* don't allow to remove root user ([019ce80](https://github.com/filebrowser/filebrowser/commit/019ce80fc529a0437984fdc3d1ab6916f34dd594))
* double click to zoom pics in phone's browser ([#1274](https://github.com/filebrowser/filebrowser/issues/1274)) ([f1b7bd5](https://github.com/filebrowser/filebrowser/commit/f1b7bd59f67e719b7bfd203b0d7ec016fd21ab49))
* environmental variables not expanded in command ([#1241](https://github.com/filebrowser/filebrowser/issues/1241)) ([f3afd5c](https://github.com/filebrowser/filebrowser/commit/f3afd5cb79d6ad8b9cc8d54cb8fc2344b7c07d3d))
* fetch resource api once when sorting (closes [#1172](https://github.com/filebrowser/filebrowser/issues/1172)) ([#1202](https://github.com/filebrowser/filebrowser/issues/1202)) ([05bb7c8](https://github.com/filebrowser/filebrowser/commit/05bb7c85531349f3e9d1d8a523bb1243587b2ebc))


### Build

* use make for building the project ([#1304](https://github.com/filebrowser/filebrowser/issues/1304)) ([23f8464](https://github.com/filebrowser/filebrowser/commit/23f84642e6c1e07f89f98d2c1bb6fc9da36cc71c))

## [2.11.0](https://github.com/filebrowser/filebrowser/compare/v2.10.0...v2.11.0) (2020-12-28)


### Features

* add sharing management ([#1178](https://github.com/filebrowser/filebrowser/issues/1178)) (closes [#1000](https://github.com/filebrowser/filebrowser/issues/1000)) ([677bce3](https://github.com/filebrowser/filebrowser/commit/677bce376b024d9ff38f34e74243034fe5a1ec3c))
* download shared subdirectory ([#1184](https://github.com/filebrowser/filebrowser/issues/1184)) ([fb5b28d](https://github.com/filebrowser/filebrowser/commit/fb5b28d9cbdee10d38fcd719b9fd832121be58ef))


### Bug Fixes

* check user input to prevent permission elevation ([#1196](https://github.com/filebrowser/filebrowser/issues/1196)) (closes [#1195](https://github.com/filebrowser/filebrowser/issues/1195)) ([f62806f](https://github.com/filebrowser/filebrowser/commit/f62806f6c9e9c7f392d1b747d65b8fe40b313e89))
* delete extra remove prefix ([#1186](https://github.com/filebrowser/filebrowser/issues/1186)) ([7a5298a](https://github.com/filebrowser/filebrowser/commit/7a5298a7556f7dcc52f59b8ea76d040d3ddc3d12))
* move files between different volumes (closes [#1177](https://github.com/filebrowser/filebrowser/issues/1177)) ([58835b7](https://github.com/filebrowser/filebrowser/commit/58835b7e535cc96e1c8a5d85821c1545743ca757))
* recaptcha race condition ([#1176](https://github.com/filebrowser/filebrowser/issues/1176)) ([ac3673e](https://github.com/filebrowser/filebrowser/commit/ac3673e111afac6616af9650ca07028b6c27e6cd))

## [2.10.0](https://github.com/filebrowser/filebrowser/compare/v2.9.0...v2.10.0) (2020-11-24)


### Features

* add hide dotfiles param  ([#1148](https://github.com/filebrowser/filebrowser/issues/1148)) ([10e399b](https://github.com/filebrowser/filebrowser/commit/10e399b3c3dbdcfb4465a9d4138e1da6bae0873d))
* add single click mode ([#1139](https://github.com/filebrowser/filebrowser/issues/1139)) ([e8b4e9a](https://github.com/filebrowser/filebrowser/commit/e8b4e9af46d6e99dbeb965dd9727d9ed017d52a2))
* automatically jump to the next photo when deleting while previewing ([#1143](https://github.com/filebrowser/filebrowser/issues/1143)) ([9515cee](https://github.com/filebrowser/filebrowser/commit/9515ceeb42e5ef5267400220a2082dec775e843d))
* shared folder file listing ([e119bc5](https://github.com/filebrowser/filebrowser/commit/e119bc55ea82cefcbcc0571650107dfd5d73f570))
* shared item information ([36cacdf](https://github.com/filebrowser/filebrowser/commit/36cacdf598e4e09f064c8ace0ca7a6c24b23028e))


### Bug Fixes

* empty folder in archive ([7096b3d](https://github.com/filebrowser/filebrowser/commit/7096b3dab92441981c9964e4a6175af0a255d2be))
* fix hanging when reading a named pipe file (closes [#1155](https://github.com/filebrowser/filebrowser/issues/1155)) ([586d198](https://github.com/filebrowser/filebrowser/commit/586d198d47b525eeccc6fe587573a3ad83adb4f6))
* previewer title overflow ([4e48ffc](https://github.com/filebrowser/filebrowser/commit/4e48ffc14d09dabeea12dc495144277db62b5b7d))
* resource rename action invalid path ([1ce3068](https://github.com/filebrowser/filebrowser/commit/1ce3068a99c80c153fd41359255d173bce6e79e8))

## [2.9.0](https://github.com/filebrowser/filebrowser/compare/v2.8.0...v2.9.0) (2020-10-21)


### Features

* support WKWebview custom protocol ([#1113](https://github.com/filebrowser/filebrowser/issues/1113)) ([0ac80e8](https://github.com/filebrowser/filebrowser/commit/0ac80e8387a69924284259bde448af2813d84ed1))


### Bug Fixes

* allow start from Windows explorer ([f2c4e78](https://github.com/filebrowser/filebrowser/commit/f2c4e78381610879eda5316d38a999c89df6c14a))
* file upload missing path slash ([5e27ba5](https://github.com/filebrowser/filebrowser/commit/5e27ba5c8c1be603c6ae7fec8de48e3532dea1f7))
* preview case sensitive file extension ([05bff54](https://github.com/filebrowser/filebrowser/commit/05bff54b71543fd232f1089c40504d0cbfd106be))
* search missing path slash ([2bd163d](https://github.com/filebrowser/filebrowser/commit/2bd163d92a856d65c8d4615e37898470c1edf2f4))

## [2.8.0](https://github.com/filebrowser/filebrowser/compare/v2.7.0...v2.8.0) (2020-10-05)


### Features

* add disable exec flag ([#1090](https://github.com/filebrowser/filebrowser/issues/1090)) ([97693cc](https://github.com/filebrowser/filebrowser/commit/97693cc6117ce1c956baede91de5dd48b904e175))


### Bug Fixes

* empty commands setting ([c6d4fcd](https://github.com/filebrowser/filebrowser/commit/c6d4fcd08f5f1531c2cef514dc86019e23e7289f))
* file upload path encoding ([babd778](https://github.com/filebrowser/filebrowser/commit/babd7783afe85b790e1c558375d7b5013b2d366f))
* fix empty command name ([#1106](https://github.com/filebrowser/filebrowser/issues/1106)) ([36fb9f5](https://github.com/filebrowser/filebrowser/commit/36fb9f562a2c005ca4390fdebde0b4690201dff9))
* fix panic when accessing nonexistent .js file in static path ([#1105](https://github.com/filebrowser/filebrowser/issues/1105)) ([ad99bf1](https://github.com/filebrowser/filebrowser/commit/ad99bf180197e0e6d82231a86457585de16366a8))
* preview key shortcut conflict ([dd7b9dd](https://github.com/filebrowser/filebrowser/commit/dd7b9ddd8546361060ef99e838a691b2fc6c495a))
* search results absolute url ([26d62e4](https://github.com/filebrowser/filebrowser/commit/26d62e411716a5eb9a5a703e47484cfb3fbf3bd0))

## [2.7.0](https://github.com/filebrowser/filebrowser/compare/v2.6.2...v2.7.0) (2020-09-11)


### Features

* add --socket-perm flag to control unix socket file permissions (closes [#1060](https://github.com/filebrowser/filebrowser/issues/1060)) ([65ac734](https://github.com/filebrowser/filebrowser/commit/65ac73414fadc4686c94803a93ff319e8f7ce9d1))
* preview mobile dropdown ([7787344](https://github.com/filebrowser/filebrowser/commit/778734419de314d4cb64d07109bbab73f8e2e42a))
* preview size button ([3d2cb83](https://github.com/filebrowser/filebrowser/commit/3d2cb838d111ee61047599f49e76de80c821f341))
* put selected files in the root of the archive (closes [#1065](https://github.com/filebrowser/filebrowser/issues/1065)) ([8142b32](https://github.com/filebrowser/filebrowser/commit/8142b32f3865eccd3331328e0d087f805d186ed5))

### [2.6.2](https://github.com/filebrowser/filebrowser/compare/v2.6.1...v2.6.2) (2020-08-05)

### [2.6.1](https://github.com/filebrowser/filebrowser/compare/v2.6.0...v2.6.1) (2020-07-28)


### Bug Fixes

* delete cached previews when deleting file ([f5d02cd](https://github.com/filebrowser/filebrowser/commit/f5d02cdde97923b963878abf5a300393b9feb348))
* escape special characters in preview url (closes [#1002](https://github.com/filebrowser/filebrowser/issues/1002)) ([c9340af](https://github.com/filebrowser/filebrowser/commit/c9340af8d045671ad3338c5d2d887c335ab92de4))

## [2.6.0](https://github.com/filebrowser/filebrowser/compare/v2.5.0...v2.6.0) (2020-07-27)


### Features

* add lazy load of image thumbnails ([bc00165](https://github.com/filebrowser/filebrowser/commit/bc001650944ae963b12b5b2538a68de7cd0d8f82))
* add param to disable img resizing ([aa78e3a](https://github.com/filebrowser/filebrowser/commit/aa78e3ab1fcae6f618e811ba4e315a7a209f9df2))
* cache resized images ([95bc929](https://github.com/filebrowser/filebrowser/commit/95bc92955f391ece22c40d9592f2a3e6e26907b9))
* limit image resize workers ([94ef596](https://github.com/filebrowser/filebrowser/commit/94ef59602fb50fc21b1164feda90a3b9aeb5e972))


### Bug Fixes

* conflict handling on upload button ([f228fa5](https://github.com/filebrowser/filebrowser/commit/f228fa55408824618e9f0879da67c86d22b0d324))
* drop feedback ([f2d2c1c](https://github.com/filebrowser/filebrowser/commit/f2d2c1cbf85fba3edffb7b079f121ed3f0bc1e02))
* missing error message ([d9be370](https://github.com/filebrowser/filebrowser/commit/d9be370e2474b8070fa58db920c9481270cc4a48))
* parent verification on copy ([727c63b](https://github.com/filebrowser/filebrowser/commit/727c63b98e2964d0960d25914c296570f6c79478))
* path separator inconsistency on rename ([34dfb49](https://github.com/filebrowser/filebrowser/commit/34dfb49b719c948e709a4639b4af2c5cb73b3887))

## [2.5.0](https://github.com/filebrowser/filebrowser/compare/v2.4.0...v2.5.0) (2020-07-17)


### Features

* add previewer title and loading indicator ([716396a](https://github.com/filebrowser/filebrowser/commit/716396a726329f0ba42fc34167dd07497c5bf47c))
* duplicate files in the same directory ([43526d9](https://github.com/filebrowser/filebrowser/commit/43526d9d1a8c837245e3f5059e0b4737583eeaeb))
* file copy, move and paste conflict checking ([eed9da1](https://github.com/filebrowser/filebrowser/commit/eed9da1471723ed3fbe6c00b1d6362b1c5fd8b04))
* rename option on replace prompt ([2636f87](https://github.com/filebrowser/filebrowser/commit/2636f876ab8f88eea6d9548de524ca2339eb0843))
* upload queue ([6ec6a23](https://github.com/filebrowser/filebrowser/commit/6ec6a2386173410f5cab9941dbf1bacb6b70ddd2))


### Bug Fixes

* blinking previewer ([9a2ebba](https://github.com/filebrowser/filebrowser/commit/9a2ebbabe2e9f0c292701d33f36f9b7a457b1164))
* dark theme colors ([b3b6445](https://github.com/filebrowser/filebrowser/commit/b3b644527d5673e16e61d404ff58a3c7bd6b6637))
* directory conflict checking ([7e5beef](https://github.com/filebrowser/filebrowser/commit/7e5beeff464e75ab185c430cd96e7cc67209ccc1))
* prompt before closing window ([194030f](https://github.com/filebrowser/filebrowser/commit/194030fcfcf54a2cf5e2f8ececcbb4754474d8f8))
* remove incomplete uploaded files ([0727496](https://github.com/filebrowser/filebrowser/commit/0727496601a9918c8131c56f62419bfac7ac589a))
* reset clipboard after pasting cutted files ([10570ad](https://github.com/filebrowser/filebrowser/commit/10570ade442b573ebe00af08369e28b1b0688df6))

## [2.4.0](https://github.com/filebrowser/filebrowser/compare/v2.3.0...v2.4.0) (2020-07-07)


### Features

* full screen editor ([0d665e5](https://github.com/filebrowser/filebrowser/commit/0d665e528f880ceda0976ceed66070ac34de7969))


### Bug Fixes

* add preview bypass for .gif files ([#1012](https://github.com/filebrowser/filebrowser/issues/1012)) ([453636d](https://github.com/filebrowser/filebrowser/commit/453636dfe2bbf177c74617862eb763485d4774bf))
* prompt key shortcut conflict ([0d69fbd](https://github.com/filebrowser/filebrowser/commit/0d69fbd9a342aa2695859021df0c423e3ae4a4fa))

## [2.3.0](https://github.com/filebrowser/filebrowser/compare/v2.2.0...v2.3.0) (2020-06-26)


### Features

* add image thumbnails support ([#980](https://github.com/filebrowser/filebrowser/issues/980)) ([6b0d49b](https://github.com/filebrowser/filebrowser/commit/6b0d49b1fc8bdce89576ba91cc0b8ec594fcd625))


### Bug Fixes

* typo in image_templates (apline -> alpine) ([#1005](https://github.com/filebrowser/filebrowser/issues/1005)) ([84da110](https://github.com/filebrowser/filebrowser/commit/84da11008516a371fc0446d97863dc14d337aa25))

## [2.2.0](https://github.com/filebrowser/filebrowser/compare/v2.1.2...v2.2.0) (2020-06-22)


### Features

* add alpine and debian docker images ([66863b7](https://github.com/filebrowser/filebrowser/commit/66863b72f7664e6cb9417f7da542a92fa77ca635))
* add folder upload ([#981](https://github.com/filebrowser/filebrowser/issues/981)) ([8977344](https://github.com/filebrowser/filebrowser/commit/89773447a56675b298394149d7a05c5df4039f14)), closes [filebrowser/filebrowser#741](https://github.com/filebrowser/filebrowser/issues/741)
* add key shortcuts ([95316cb](https://github.com/filebrowser/filebrowser/commit/95316cbe8c8ac3dbb28310bc11ec347c0caf699b))
* upload progress based on total size ([#993](https://github.com/filebrowser/filebrowser/issues/993)) ([cd454ba](https://github.com/filebrowser/filebrowser/commit/cd454bae51f40b1249e6fa6133c2949970eb3018))


### Bug Fixes

* add a workaround to fix window freezing when viewing a large file [#992](https://github.com/filebrowser/filebrowser/issues/992) ([2412016](https://github.com/filebrowser/filebrowser/commit/241201657c2bf01806d02a297eb846b26102a479))
* apply all fs user rulles ([68f8348](https://github.com/filebrowser/filebrowser/commit/68f8348ddeecba570a361e7aba4546052cc3e356))
* frontend token validation ([dd40b0d](https://github.com/filebrowser/filebrowser/commit/dd40b0d9b9cc6268a611306ac4684a1af852b79d)), closes [filebrowser/filebrowser#638](https://github.com/filebrowser/filebrowser/issues/638)
* multiple selection count ([963837e](https://github.com/filebrowser/filebrowser/commit/963837ef1dc6e2e84fcf924606ce388ac30f3891))
* save event hook ([82c883f](https://github.com/filebrowser/filebrowser/commit/82c883f95eead9eebe215e230f74773c945f864a)), closes [filebrowser/filebrowser#696](https://github.com/filebrowser/filebrowser/issues/696)