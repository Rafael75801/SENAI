* Update translations: ca, de_AT, en_GB, eo, id, ko, pt_PT, sk, sq.
* Add python-cffi to the Windows AIO build script.
* Remove check that path exists in the media path unit test. Fixes #13305.
* Simplify logic for setting data, config and cache directories.
  Fixes #13261, #13686.
* Migrate data from old the directory structure. Fixes #13300.
* Fix nested transaction error in the Test Case Generator tool. Fixes #13680.
* Enable Web Connection menu in all list views.
* Fix schema upgrade errors. Fixes #13674.
* Add database upgrade unit tests.
* Package Gramps-6.0.0-rc1 for macOS.

2025-03-02
Version 6.0.0-rc1
* Update translations: ca, cs, da, de, de_AT, en_GB, eo, fi, fr, he, hr, hu, id,
  ko, mk, nb, nl, pt_PT, ru, sk, sv, ta, tr, uk.
* Add selenium to Windows AIO build.
* Simplify RelationshipPathBetween prepare method.
* Simplify HaseSourceOfBase prepare method.
* Fix upgrades from bsddb. Fixes #13633, #13652.
* Always return str from to_string methods.
* Fix bug with surname rules in Quick Views. Fixes #13657.
* Reformat code using the latest stable version of black.
* Strip whitespace from media path in media editor.
* Strip whitespace from name and URL in Addon Manager project editor.
* Provide new editor fallback icons for superscript and subscript. Fixes #13548.
* Change default preferences to be more appropriate for new users.
* Add extra checks when changing a parent in the family editor.  Fixes #13642.
* Hide navigation bar selector when only one sidebar plugin is loaded.
  Fixes #13640.
* Fix media manager bug with relative to absolute path conversion. Fixes #13644.
* Fix bug removing citation references after deleting a source. Fixes #13639.
* Update the web search URL so that it works.
* Remove the default toolbar style option and replace it with "Both".
* Fix citation filter rules that search the source. Fixes #13635.
* Fix crash in source/citation selector with an empty filter. Fixes #13634.
* Convert deprecated filter operator "xor" to its synonym "one".
* Mac:
  * Package release 6.0.0-beta2 on macOS.
  * Update dependency versions, bundle contents.
  * Remove python-fontconfig from the build, no longer used.

2025-02-12
Version 6.0.0-beta2
* Update translations: cs, de, de_AT, fi, he, hr, hu, is, it, nl, pl, pt_PT, sk,
  sv.
* Narrative web:
  * Add remote media to thumbnail index.
  * Remote media cannot be opened.  Fixes #13628.
  * Fix crash with empty an database.  Fixes #13619.
  * Fix to show tree on print page. Fixes #13614.
  * Correctly handle Event == None.
* Windows AIO:
  * Set appbuild correctly.
  * Add a build-number input to the workflow.
  * Remove the "-- a new maintenance release" branding from the installer.
* Mac:
  * Remove obsolete gtkspell3 from bundlefile. We're using gspell now.
  * Package Gramps 6.0.0-beta1 for macOS.
* Center the progress bar in the main window status bar. Fixes #13630.
* Fix bug in generic filter (swapped lines).
* Fix the program name in the About dialog.
* Remove BSDDB version and duplicate Gramps version from About dialog.
  Fixes #13624.
* Rename "Help" button to "Wiki" in plugins dialog. Fixes #13625.
* Change the progress bar vertical alignment and padding. Fixes #13623.
* Import annotations in files using type hints.
* Specify the `obj_class` when calling `data_to_object.`
* Fix crash during bsddb upgrade. Fixes #13627.
* Fix error when upgrading a database from 5.1 to 6.0. Fixes #13622.
* Ignore missing remote media in check and repair tool. Fixes #13618.
* Don't try to run `get_git_version` in release versions.
* Correct the parameter type hints to accept <object> | None.
* Private proxy fixes.
* Fixed an iter that bypasses proxy.
* Fix modifiers in Hungarian date handler.
* Added orjson, and 'all' to the setup script.
* Updated the README (bsddb3 made optional, removed sqlite3).
* Fix the match method in the GenericFilter class. Fixes #13606.
* Replace unittest `assertEquals` by `assertEqual`.
* Fix type annotation syntax for Python 3.9.
* Fix error when searching by name in the place selector. Fixes #13605.
* Enable <Enter> key press on date fields in sidebar filters. Fixes #13607.
* Fix all_people() simple access method to use new data format Fixes #13603.
* Translation fixes in probably alive code. Fixes #13604.
* Update CI workflow to run on the gramps60 branch.

2025-02-04
Version 6.0.0-beta1
* Update translations: ar, bg, br, ca, cs, da.po, de, de_AT, el, en_GB, eo, es,
  fa, fi, fr, ga, gl, he, hr, hu, id, is, it, ja, ko, lt, mk, nb, nl, nn, pl,
  pt_BR, pt_PT, ro, ru, sk, sl, sq, sr, sv, ta, tr, uk, vi, zh_CN, zh_HK, zh_TW.
* Update development status classifier.
* Update translation template for new release.
* Fix xgettext format string.
* Add missing files to `POTFILES.in`.
* Fix accessing an attribute in a DataDict.
* Add missing future import for annotations.
* Add type hints to modified functions.
* Optimise get_object_from_gramps_id methods in filter proxy.
* Refactor, fix, and optimize filters/rules.
* Add GrampsID type hints to DbGeneric.
* Define types for Gramps IDs.
* Add licence and copyright.
* Make the orjson package mandatory.
* Use orjson with a hand-coded encoder/decoder. Assumes orjson is installed.
* Disable pylintrc no-else-return check.
* Allow web-accessible file references in media objects.
* Add type hints to the generic database handler.
* Update Info.plist for Gramps 6.0. The important change is that macOS 11.0 is
  now the minimum required for both Intel and Apple Silicon Macs.
* Add heatmap to the narrative web report.
* Memorise report options for each database. Fixes #2455
* Add help_url to built-in tools.
* Add help button to plugin selection dialogs. Issue #13467.
* Enhance display_help utility function:
  * Allow the webpage to include a section separated by a hash (#) character.
  * Allow a webpage starting with http:// or https:// to specify a full url.
  * Add unit tests. Fixes #13562.
* Update minimum python version.
* Add type hints to latitude and logitude related methods and functions.
* Use attributes rather than dictionary lookup in the model classes.
* Crash with empty ADDR in narrative web. Fixes #13479
* New indexes for big databases in the narrative web report.
* Correct the tab name for setting the date format in a Tip of the Day.
* Remove unnecessary translations.
* Fixes to probably alive code following reviewer comments.
* Fix safe mode on Windows Safe mode.
* Make cleanup optional after an AIO build.
* Add type information to base selector.
* Use search bar filters instead of fast filter classes.
* Search bar filter has precedence.
* Add the standard search bar to the SelectPerson dialog.
* Add a preference option for the selection of the toolbar style.
* Use ngettext when displaying the max probably alive age in years.
* Rephrase the citation references option in the narrative web report.
* The example filename in the welcome gramplet should not be translated.
* The space used as an empty column heading does not need translation.
* Add a translation context to a couple of name origin types.
* Use ngettext in probably alive function.
* Remove unreachable else statement in probably alive code.
* Fix "alt_names" typo in the place model.
* Add new place to example database.
* Fix date modifiers for is.
* Fix de_AT translation.
* Change http:// to https:// in Tip of the Day file.
* Strongly recommend orjson in the README.
* Add orjson version strings.
* Add orjson dependency to Windows AIO.
* Add orjson dependency to Mac bundle.
* Use orjson, if available.
* Fix exact search filters in selector dialogs.
* Allow importing and exporting nicknames to CSV.
* Replace assert statements with TestCase methods in unit tests.
* Fix python format string related xgettext warnings.
* Fix narrative web when a person excluded by a proxy is referenced.
* Recognize event reference citations in editor event tabs.
* Display the source icon in the event tab of an editor if the event has either
  an event citation or event reference citation.  Fixes #13401.
* Fix AttributeError in editor surname tab. Fixes #13322
* Allow multiple selection in the gallery tab in editors.
* Allow multiple selection in the media selector dialog.
* Add optional support for multiple selction in selector dialogs.
* Merge the two different MultiTreeView classes.
* dd path column to the media selector dialog.
* Remove serialize from changenames.
* Create DataDict from object; Get object with from_dict():
  * Allow construction of a DataDict from an instance.
  * Clean up DataDict a bit * Return object instance from_dict() if it exists.
* Improve language and hamburger menus in narrative web report:
  * Improve the backlinks (References) gramplets
  * Enhance ListModel to handle middle mouse clicks.
  * Allow an object to be made active from within the backlinks gramplet.
  * Add a context menu to make "Edit" and "Make Active" more discoverable.
  * Allow objects in the backlinks gramplets to be dragged to the clipboard.
  * Display the Date column for all objects which are an instance of DateBase.
* Fix exception during Redo operation.
* Set initial focus in EditPlaceRef dialog.
* Add edit capability to the set of Notes gramplets.
* Update the gramplet display when a note is updated, added or deleted.
* Use Ubuntu 22.04 for CI.
* Add gender symbol option to the detailed descendant report.
* Add gender symbol option to the detailed ancestral report.
* Add gender symbol option to the descendant report.
* Add an option to insert a gender symbol before the person's name.
* Enable mypy static type checking.
* Remove trailing whitespace check. This is now performed by black.
* Fix the spelling of "because" in comments.
* Refactor GrampsType set method to use functools.singledispatchmethod.
* Convert images in tree reports to thumbnails for embedding.
* Improve the ProbablyAlive code. Implements #13443.
* Update bundle for gspell, new enchant.
* Convert 'Tip of the Day' window to `Gtk.Template`.
* Add PyPI upload workflow.
* Change variable name to 'data' for consistency across the code base.
* Fix error in Fast*Filter.
* Update GrampsType to work with dict objects.
* Replace deprecated 'warn' method with 'warning'.
* Replace deprecated makeSuite with TestLoader().loadTestsFromTestCase.
* Skip TestImports if en_US locale is not available on build host. Fixes #13079.
* Fix unittest for local timezones.
* Update Debian build to include Ubuntu 24.04.
* Add new HasEvent and HasSource rules.
* Translate the filter comment string.
* Use css error class rather then hardcoding the colour "red".
* Enhanced version of the Filter gramplet.
* Add new 'having note of type' rule.
* Change layout of places and dates in familylines plugin. Adds symbols and
  changes format of birth and death events. Implements #7788, #10699.
* Show other roles for an event in the narrative web report.
* Harmonize Date Format label capitalization.
* Add link to Sphinx footer add hotlink to footer for potential contributors.
* Add missing tooltips in the Addon Manager Implements #13358.
* Add Gramps ID option to Kinship Report.
* Allow Gramps to run from an extracted source distribution.
* Use standard decorator form of defining properties.
* Replace deprecated Gdk.Color by Gdk.RGBA.
* Fix deprecation on ElementTree truth testing.
* Stop displaying Python-sqlite3 version.
* implify multiple calls to `str.startswith` / `str.endswith`.
* Remove redundant definition of _has_webpage_extension.
* Use contextlib to redirect stdout/stderr.
* Remove deprecated use-action-appearance property.
* Remove stock items from Glade files.
* Fix xalign deprecations in Glade files.
* Fix margin-* deprecations in Glade files.
* Added 11k serialize tests.
* Added a dict wrapper that acts like an object.
* Switch from pickled blobs to JSON data.
* Store empty date objects instead of null in the JSON schema.
* Refactor JSON serialization.
* Make BaseObject the parent class for Date, StyledText and StyledTextTag.
* Add PyPI upload workflow.
* Some filter rule type related cleanups.
* Add new role types present in the Gedcom 7.0 specification.
* Replace deprecated Gtk[HV]Box with GtkBox.
* Add support for ISO 639-3 part 3 standard language code. Fixes #12772.
* Change the output of ADDR tags in the Gedcom export.
* Use preferred name instead of default name in name editor. Fixes #13256.
* Prevent forwards/backwards when history is locked.
* Add forwards and backwards navigation using mouse buttons.
* Pylint cleanups for gen/db/*.py.
* Some pylint cleanups for gramps/gen/plug/*.py.
* Pylint cleanups for plugins/db/dbapi/*.py.
* Pylint cleanups for gen/lib/*.py:
  * Reformat to default 88 columns and factor out EventBase.
  * Use of _ is cleaner for unreferenced vars.
* Allow 0 ancestors/descendants in hourglass graph.
* Sort AIO prerequisites + remove unneeded.
* Simplify some Cairo drawing.
* Remove unused Subversion keyword substitutions.
* Replace GtkMenu with GioMenu in DropdownSidebar.
* Convert navigator from a Notebook to a Stack.
* onvert navigator menu into a combo box.
* Fix typo in Navigator action/section id.
* Remove unused code from Navigator.
* Replace GtkMenu with GioMenu in Gramplets bar.
* Replace GtkArrow with GtkImage and symbolic icons.
* Update format of Glade files.
  * Glade files regenerated using 3.40.0.
  * Required Gtk version set to 3.24.
* Restrict CI workflow to run on a single branch.
* Update GitHub actions to latest versions.

2025-01-12
Version 5.2.4
* Translations:
  * Updated translations: bg, cs, da, de, de_AT, en_GB, es, fa, fi, fr, he, hr,
    hu, id, ko, mk, nb, nl, pl, pt_PT, sk, sl, sv, ta, tr, uk, zh_CN, zh_HK,
    zh_TW.
  * Remove Tamil from this release.
  * Update translation template for new release.
  * Update list of incomplete translations.
  * Add German date modifier "ab".
  * Fix German date handler for reports. Fixes #13312.
  * Add extra "about" modifier to Hebrew date handler.
  * Add Korean translation.
  * Fix date modifiers for sl.
* Fix Citations gramplet to recognize event reference citations. Fixes #13555.
* Fix exception when finding relationship to home person. Fixes #13495.
* Fix mouse scroll direction in pedigree view.
* Fix incorrect usage of exec. As of PEP558, `locals()` is not populated by
  `exec()`. This change means that this call is broken on Python 3.13.
* Remove some usage of globals().
* Remove unnecessary use of exec.
* Test current_date being an empty date in probably alive function. Fixes #13431.
* Improve warning message in date_test.py when 3 tests are skipped.
* Correctly assign sortval = 0 when a date is EMPTY. Fixes #13415, #13423.
* Fix unicode conversion bug when upgrading from schema 16 to 17.
* Correct the documentation for the match() method of the Date class.
  Also added more detail to documentation in 3 other cases. Fixes #13428
* Gramps version output now reports OS rather than Platform. Fixes #12285.
* Downgrade upgrade messages from warning to informational level. Fixes #13464.
* Fix list size option in the top surnames gramplet. Allow users to specify how
  many surnames appear in the list from 10 to 1000. Fixes #13448.
* Correct misleading description of GUI element placement.
* Use the preferred calendar for new dates only in the date editor. Fixes #13403.
* Fix docs typo in INSTALL file.
* Fix printing of Books. Fixes #12804.
* Render reports with styled notes containing subscript and strikethrough.
  Fixes #13417.
* Remove broken link to svn2cl package in the About dialog. Fixes #13152.
* Improve media performance in the narrative web report. Fixes #13370.
* Mac:
  * Replace gtkspell3 with gspell.  Fixes #13514.
  * Upgrade json-glib to fix a build failure with recent glib versions.
* Windows AIO:
  * Restore AIO console executable's icon. Fixes #13402.
  * Fix spelling in a comment.
  * Remove UPX compression of exectuable files.
  * Remove commented out line.
  * List packages in alphabetical order for easier maintenance format document.
  * Improve grammar.
  * Ensure library.zip is generated by cx_freeze.
  * Update copyright date.
  * Use a virtual python environment. This allows pip to work correctly.
  * Prefer to use base_exec_prefix.
  * Changes required due to updating MSYS2 environment.
  * Remove references to lib2to3 (deprecated).
  * Reduce log output from build.sh so errors and warnings are easier to spot.
  * Cleanup README.
  * Prevent debug plugins loading for Gramps AIO.
  * Reduce output in log files for easier parsing.
  * Downgrade cx_Freeze in Windows AIO to 6.15.9

2024-07-13
Version 5.2.3
* Updated translations: da, de_AT, en_GB, es, fr, he, hr, hu, mk, nb, nl, pt_PT,
  ru, tr, zh_HK, zh_TW.
* Fix bug with regular expressions in check_po script.
* Update translation template for new release.
* Corrected terminology. Replaced "matronymic" with "matrilineal" to accurately
  reflect genetic inheritance rather than naming conventions.
* Clarified terminology for father lineage description. Changed
  "patronymic lineage" to "patrilineal lineage" for accuracy.
* Fix PDF generation failure with LaTeX-based reports on Windows. Fixes #10696.
* Fix fallback for the `image_size` utility function Use Gdk if the size of the
  image cannot be determined by imagesize.  Fixes #13310.
* Disable rounding glyph positions in cairo document generator.
* Package Gramps 5.2.3 for macOS.
* Fix NoteType values in CSV import.
* Some short french month names can not be entered.  Fixes #13307.
* Remove detached process flag when running lualatex.
* Check that pdf output file exists in genealogy tree reports. Fixes #10696.
* Fix error when changing the style of misspelt words. In the note editor,
  changing the style of text failing the spell check caused an error.
  Fixes #13282.
* Update span characters for zh_TW. Add span characters so that the new display
  format is accepted as a valid input format.
* Restore BerkelyDB, Gramps still uses it.
* Update gramps.modules.
  * Remove obsolete comment and comment out the private include.
  * Update the branch in gramps-git.
  * Remove BerkeleyDB and pybsddb dependencies.
  * Remove unused patches.
* Fix missing media in narrative web report person pages. Fixes #13252, #13272.
* Remove the spaces padding the connector in a hyphenated surname. This fixes
  the previous code which replaced " - " with "-" within the entire name.
  Fixes #13274.
* Url-quote norm_path and use urljoin to attach the scheme.  Assumes that if
  the path is already a URI it is also already quoted.  Fixes #13218, #13197.
* Prevent hyperlink tagging being added as an undo action. Clicking the undo
  button in the note editor sometimes had no noticeable effect.  Fixes #13267.
* Change repository "Title" to "Name" in the source editor.  Fixes #13258.
* Better error handling in the narrative web report.
* Handle not found when creating the narrative web report updates page.
  Fixes #13216.
* Add workflow for Debian build.
* Package Gramps 5.2.2 for macOS.
* Use README.md for PyPI long description.
* Fix Windows AIO build.

2024-04-06
Version 5.2.2
* Updated translations: cs, de, de_AT, es, fi, he, hr, nb, nl, pl, ru, sk, sv,
  tr.
* Hebrew relationship calculator not loading. Fixes #13251.
* Narweb: Person object has no get_father_handle. Fixes #13207.
* Package Gramps 5.2.1 on macOS.
* Restrict CI workflow to run on a single branch.
* Don't show Navigation when we print a page.  Fixes #13160.

2024-03-24
Version 5.2.1
* Updated translations: de_AT, fi, fr, ga, he, it, nb_NO, pl, sk, sr, tr, uk,
  zh_Hans.
* Fix error when installing an addon that will not be registered. Fixes #13233.
* Allow experimental and beta plugins to be registered. Fixes #13232.
* Tidy up the README file.
* Fix fan charts on HiDPI screens.
* Replace PIL with Pillow in the README. Issue #10016.
* Fix the Tag.is_empty() method. The `Tag.is_empty()` method was returning the
  inverse of the expected value. Fixes #12579.
* Cannot create Place with coordinates via Geography. Fixes #13228.
* Fix place title when place names use open spans. Fixes #13222.
* Fix the addon translator language for core translations. Fixes #13221.
* Update AIO minimum Windows version requirement to 8.1 64-bit.
* Prevent unwanted output in unit test logs.
* Fix unit tests when run with Python 3.12. Fixes #13212.
* Revert Death fallback symbol from Latin Cross to "+".
* Change the cross mark and check mark symbols used in the Addon Manager.
  Requirements screen to be valid characters on Mac. Fixes #13194.
* Fix display of invalid dates in editor citation tabs. Fixes #13192.
* Include metainfo rather than appdata 'its' files.
* Update AppStream MetaInfo file to conform to latest spec.
* Fix filter rules missing the use_case parameter. Fixes #13187.
* Rename metadata file to follow spec.
* Add release information to appdata.
* Package Gramps 5.2.0 on macOS.

2024-02-23
Version 5.2.0
* Updated translations: ca, cs, da, de, de_AT, en_GB, es, fr, hr, hu, id, it,
  nb, nl, pl, sk, sl, sv, tr, uk, zh_CN.
* Update development status to production.
* Remove the Trove classifier "Natural Language :: German(Austrian)".
* Emit a "plugins-reloaded" signal when a new addon is installed. This ensures
  that the user interface will be updated to include the new addon.
  Fixes #13021.
* Fix Windows AIO build.
* Update GitHub actions to latest versions. Some actions are deprecated.
* Package Gramps 5.2.0-rc1 on macOS.

2024-02-09
Version 5.2.0-rc1
* Updated translations: ar, bg, cs, da, de, de_AT, en_GB, es, fi, fr, he, hr,
  mk, nb, nl, pl, pt_PT, ru, sk, sr, sv, tr, uk, zh_CN.
* Add Hebrew relationship calculator.
* Add Hebrew date handler.
* Refine Hebrew About modifiers in date parser.
* Add Hebrew to the list of user manual translations.
* Update copyright dates.
* Windows AIO:
  * Improve AIO build script to run without modifications. The build script
    required modification before first use to set the full path to the local
    aio directory. Second change is to use the `-N` option in wget to avoid
    downloading a file if the timestamp hasn't changed on the server. Third
    change is to avoid the script from asking for interactive input on second
    and subsequent runs.
  * Add pip.exe and Adwaita scalable icons to Windows AIO.
  * Fix up Windows AIO for pip, and Finnish spell check.
  * Ignore AIO build artifacts in .gitignore file.
* Addon Manager:
  * Invalidate caches after new python modules are installed. This ensures that
    any new python modules installed will be found by the python import
    mechanism.
  * Allow multiple versions in gi requirements. Enhances the `requires_gi`
    property in gpr files to allow mutiple versions of a GObject introspection
    module.  e.g. requires_gi=[("GooCanvas", "2.0,3.0")]
  * Update a couple of strings to clarify the Addon Manager UI. Fixes #13019.
  * Fix Addon Manager help link. Fixes #13018.
  * Capitalize "python" in the Addon Manager settings. Fixes #13016.
  * Fix addon prerequisites install.
  * Make the Addon Manager available without a tree loaded.
  * Change "url" to "URL" in the project editor.
  * Set default project editor window width to 600.
  * Refresh row in Addon Manager after an addon is installed. When an addon is
    installed there is no need to refresh the addon listing. We just need to
    update the row. This also keeps the user in the same place in the list.
    Fixes #13001.
  * Rename "Uninstalled" to "Not installed".
  * Add an extra requirements check after installing modules.
* Verify tool:
  * Convert the Data Verify tool to display results in a tree.
  * Add 8 more data verify rules.
  * Fix some garbage collection issues.
  * Performance enhancements.
  * Also fixed a small amount of easy pylint issues.
* Fix invalid escape sequences by doubling backslashes, or making the strings
  raw, as is commonly done for regexes.
* Make subprocess inherit environment variables in setup script. The PATH
  environment variable got unset for that subprocess, thus not being able to
  find msgfmt.
* Fix command line progress output. The text was partly overwritten whenever
  the percent value was updated. Add unit tests.
* Added HasRepo rule to rule list. Fixes #13097.
* Fix references to gramps-xml file format in man pages.  Change -f gramps-xml
  to -f gramps Fixes #9723.
* Update and fix CSV import. See discussion on the discourse forum:
  https://gramps.discourse.group/t/how-can-people-be-deleted-according-to-a-list/4511/13?u=dsblank
* Fix gramps example media source.
* Clarify the Tip of the Day text to indicate that it applies specifically to
  "Grouped People View", not the flat People View.  Fixes #12897.
* Report simpler Python version string in About and Error dialogs.
* Fix DeprecationWarning for invalid escape sequence. Change to use raw string.
* Fix invalid file mode error with Python 3.11.
* Fix hyphenated surnames in name displayer. Strip spaces around a hyphen,
  so for example, "Smith - Jones" is cleaned up to become "Smith-Jones".
  Fixes #13086.
* Add year rounding option to preferences. Fixes #12422.
* Fix context menu in all family events quick view screen. Fixes #12759.
* Added option to display birth and death info in descendant report.
  Implements #12758.
* Update Doug Blank's email address.
* Add new event reference citations to the private proxy.
* New citations not included on the Narrative Web. Fixes #13046
* Add event reference citations to the complete individual report. Fixes #13035.
* Fix display of gramplet help URLs that start with "https://". A help_url
  starting with either "http://" or "https://" should be used as the full url
  to be displayed in the browser.  Fixes #13039.
* Fix bug in narrative web when the role name contains a dash. Not enough values
  to unpack in sort_by_role. Fixes #13042.
* Make the narrative web support both LTR and RTL layouts. Fixes #12960.
* Minor string changes to narrative web report options.
* Sort Confidence column in source citation tabs. The "Confidence level" is
  sorted by confidence label instead of the internal value. The
  "Confidence level" text is too wide and replaced by "Confidence".
  Fixes #13036.
* Fix imports test for new note added to database.
* Fix GEDCOM import for SUBN record containing note. Fixes #13024, #12152.
* Use imagesize rather than magic.
* Reformat code using the latest stable version of black.
* Fix sizing of shared information in the reference editors. Sets the packing
  of the expander widget to depend on whether or not it is expanded.
  Fixes #13030.
* Fix crash when displaying settings in context menu popup of the pedigree view.
  A separator menu item was being added twice.  Fixes #13029.
* Add help_url to built-in gramplet plugin data. Link Gramplets to new wiki
  landing anchor of lookup table which shows which Gramplets work in which
  categories.
* Add right and left margins to the welcome gramplet. Add some white space
  between the left/right text box borders and the text glyphs. See:
  https://gramps.discourse.group/t/what-can-i-do-to-help-fix-unpadded-text-gramplets/2293/2
* Rename "Ancestor View" to "Pedigree View" in Tip of the Day. Fixes #13023.
* Fix translated Tip of the Day entries with quote characters. When extracting
  strings from the `tips.xml` file, xgettext removes the escape sequence for
  the quote character (&quot;) so we don't need to add it back before we obtain
  the translated string.  Fixes #12325.
* Fix a few deprecation warnings Issue #13021.
* Fix report dialog error when no active person selected. Running a report from
  the reports dialog with no active person selected caused an error.
  Fixes #13020.
* Rename citation formatter from "Default" to "Legacy".
* Update width of Gramps ID fields in editors. These fields appeared wider in
  earlier Gtk versions. Fixes #12999.
* Replace remaining Gtk.Menu.popup calls The `popup` method is deprecated. The
  remaining calls to `popup` are replaced by `popup_at_pointer`.
* Fix positioning of popups relative to widgets. Replace `popup` with
  `popup_at_widget` and remove old positioning functions. Fixes #13008.
* Change the subscript key binding in the note editor. Use <PRIMARY>r for
  subscript. The standard keyboard shortcut for copy is <PRIMARY>c.
  Fixes #13002.
* Set filter editor rule list to expand.
* Fix display of help links in gramplet bars. Use `display_help` rather than
  `display_url` to display manual pages.
* Add more scrollbars to the Preferences dialog.
* Fix bug in endnotes citations.
* Fix bug when deleting a row from a filtered flat list view. Fixes #12995.
* Fix sizing of the surname table in the name editor. The columns were slightly
  too large requiring a scrollbar with the default dialog size and column
  widths.  Fixes #12994.
* Add missing cite and thumbnailer plugin directories to build script.
* Include javascript files in installation. Fixes #12991.
* Fix black margin in project list with scrollbar. Fixes #12993.
* Package Gramps-5.2.0-beta2 on macOS.
* Fix translator date inflection comments.

2023-08-25
Version 5.2.0-beta2
* Updated translations: ca, cs, da, de, en_GB, es, fi, he, hr, it, nb, nl, pl,
  pt_BR, pt_PT, ru, sk, sv, tr, uk.
* Add option to exclude fan chart title.
* Prevent fan chart title being overwritten by the chart. Fixes #12926.
* No longer state that Gramps will close in the backup message. Fixes #12984.
* Clean up some Gdk Screen deprecations.
* Fix Gedcom import tagging a note with an undefined tag handle. Fixes #12985.
* Fix crash when printing notes during endnote creation. Fixes #12983.
* Fix `trans_text` keyword in `xgettext`. Fixes #12982.
* Fix vertical expansion of family tree manager list.
* Fix error 404 with openstreetmap map service.
* Restrict access to Stamen maps. Fixes #12971.
* Track column width settings for all editor tabs separately.
  Fixes #12945, #12970.
* Add support for Hebrew prefixes.
* Add Farsi and Galician to Microsoft Windows Locale list.
* Add a scrolled window to the preferences data tab. Fixes #12968.
* Addon Manager:
  * Rename "Upgrade" to "Update".
  * Fix addon settings bug.
  * Add installation status filter.
  * Add project up, down and restore buttons.
  * Add help button.
* Fix error when deleting a surname. Fixes #11744, #12626, #12629, #12963.
* Fix glocale problems on Windows.
* Fix system locale detection on MS Windows.
* Add Windows AIO workflow.
* Fixes for the Windows AIO build:
  * Convert packages from python3 to python.
  * Replace `share.tgz` with downloaded files.
  * Add missing dictionaries.
  * Add missing D-Bus executable.
  * Use newly available bsddb3 package.
* Improved organization of the Addon Manager filter lists. Fixes #12958.
  * Update the plugin type names and sort them alphabetically.
  * Swap the order of "Expert" and "Developer" in the audience list.
  * Reverse the order of the status list.
* Include event reference citations and notes in Gedcom export.
* Better URLs for gramplet bar help. Fixes #12957.
* Tidy up strings in preferences.
* Fix spelling mistake in Pro-Gen importer.
* Improve Addon Manager search. Fixes #12955.
* Check for Windows executables in addon requirements. Fixes #12954.
* Do not strip checksum of media object in private proxy.
* Update po snippet generation to output msgctxt.
* Save column sizes before a rebuild. Save column sizes as floats rather than
  integers. Fixes #12943.
* Set default column size in list views to sensible defaults.  Fixes #12944.
* String improvements.
* Update authors file.
* Fix changes reverted by mistake.  This restores a couple of autobackup
  intervals and removes bsddb from the list of backends.
* Fix bottombar not saving size. Fixes #12941.
* Fix incorrect genealogical symbols. Fixes #12937.
* Mac: Use tarball for osm-gps-map instead of git repository.
* Changes for Black integration.

2023-08-01
Version 5.2.0-beta1
* Highlights
  * Create new Addon Manager dialog.
  * Add support for open spans.
  * Add strikethrough and superscript/subscript support.
  * Add new gender option of "Other".
  * Add citations to event references.
  * Deprecate BSDDB, but allow to be loaded with convert to SQLite.
  * Add coordinates format with description. Fixes #11248
  * Add the possibility of case sensitive/insensitive search.
  * Add source icon to editor dialogs. Implements #11372
  * Make the tab columns resizable. Implements #8767
  * Support XDG base directory specification. Fixes #8025
* General
  * Update README, INSTALL and FAQ files.
  * Update copyright dates.
  * Update Creative Commons license version to 4.0.
  * Minor string fixes. Add or remove whitespace.
  * Append full stops to ends of sentences. Remove full stops after ellipses.
  * Spelling fixes.
  * Many Pylint and other cleanups.
* Reports
  * Birthday and Anniversary Report: Add person ID.
  * Common calendar on Statistics chart. Fixes #12571
  * HourGlass graph: Add option to use genealogical symbols for events.
  * Statistics chart: Small code improvements.
  * Calendar report enhancements:
    * Added symbols for birth, marriage and death.
    * Added symbols for dead spouse in anniversaries.
    * Optionally include death dates.
    * Refactored method `collect_data`.
  * Added flipped text option to Graphical Report Fan Chart.  This option flips
    the names in generations 2, 3 and 4 that on the bottom half of the fan.
  * Kinship report: change max number of generations. Fixes #12004
  * Add a new primary surname substitution keyword option.
  * Add option name_format to treedoc. Implements #12136
  * Enhance name formats in the genealogytree reports.
  * Add new output format of "graph" to the tree document generator.
  * Display leap day anniversaries every year on calendars.
  * Show index of person in ancestor tree report.
  * Enable markup in ODF backend.
  * Relationship Graph: Add option for 'offset parents' Replaces 'use subgraph'
    option. Fixes #11550, #11494
  * Add fanchart option with overhang. By adding an overhang to the fanchart,
    more space can be used.
  * Do not round rotation in SVG. When making >8 generation fan charts,
    the rounding of rotation becomes visible.
  * Family group report enhancements:
    * Replace Marriage heading with relationship type.
    * Remove Husband and Wife headings. These are incorrect for same-sex
      relationships or when the couple are unmarried.  Resolves #11199
  * Complete individual report:
    * Use shorter name to reduce line length.
    * Add option that allows to use the name of the individual as title.
  * Calendar: Use the death symbol defined in preferences.
  * Add descriptions to decendant tree report styles.
* Gramplets
  * Improved Age Stats gramplet:
    * New Histogram widget.
    * Extra bucket for ages above maximum.
    * Automatic scaling to available width.
  * Image Metadata Gramplet expand metadata support:
    * Enable showing XMP and IPTC metadata.
    * Add additional metadata fields that contain tags and text descriptions.
    * Display thumbnails for XMP-mwg-rs Regions.
  * Calendar gramplet: Add day names. The first day is defined according to the
    locale. Fixes #12515
  * Allow gramplets to have an orientation dependent layout. Use this for the
    gallery gramplets.  Implements #11527
  * Update Welcome gramplet.
  * Link to translated wiki pages in welcome gramplet.
  * Add a note gramplet for NoteView.
  * Show note type in notes gramplet. Also move page number next to
    forward/back buttons.  Implements #12402
  * Add Copy All functionality to Ancestor gramplet.
  * Citations gramplet: Add date, page, and confidence. Fixes #9224
    * Change columns order and size.
    * Sort correctly by date.
  * Display the event date in the backlinks gramplet. Fixes #12230
  * AgeOnDate gramplet: Fix position of input field and button.
  * Add context menu entries for Gramplet Bar. Link to help for Gramplets and
    the Gramplet Bar Menu. Issue #10919
* Narrative Web Report
  * Sort events by date in the individual page.  Fixes #12717
  * Clarify how to get the API_KEY. Fixes #12646
  * Solves some problems. Force place name to be "Full" names. Fixes #12821
  * Add noindex for robots.
  * Lightbox feature. Feature request: #12801
  * The latest version of openlayers doesn't work:
    * Change the location of js and css files.
    * Menu simplification and usage clarification.
    * Show in which file the openlayers version should be modified.
    * Show the config name to modify.
  * Code simplification.
  * Add a comment if invalid lat/long. Fixes #12565
  * Some fixes to alphabet_navigation. Ensure correct index letters according
    to normal indexing conventions by using ICU AlphabeticIndex. Fixes #12350
  * Change order of Event Reference Notes and Notes. Fixes #12356
  * Possible loop with associated people.
  * Add option to show all places. Fixes #12315
  * Don't display media, source ref for unused place.
  * Backlink gramplet problem if no back references.
  * Show image on the map only if it was collected.
  * Show the thumbnail place if already collected.
  * Add place name to birth and death dates when we use the toggle section.
  * Possible problem with RTL languages.
  * Inconsistency between the name of the link to a reference and the name of
    this reference for an individual.  Fixes #12336
  * Translation problem + missing events on markers.
  * Addressbooklist: headers aren't translated.
  * Missing events for markers + code simplification.
  * Various fixes to user-visible strings.
  * Toggle bug for source attribute.
  * Remove the note type 'Html code' for notes. Fixes #12184
  * Add php session_start. Fixes #12135
  * Multiple languages for the narrative web and optional other additions
  * Fix letters in comment:
    * Insert missing letters in comments.
    * Terms to upper case (gregorian, javascript).
  * In cms mode, some inconsistent image links.
  * Incorrect place index if alternate names. The places page index doesn't
    show the alternate names used. Fixes #11645
  * Description message is not translatable.
  * Possibility to have more than 2 downloads. By default, I set this to
    3 downloads. Fixes #11626
  * Add family map to family pages. Adapt css files to have a better look.
    Fixes #11614
  * Set unused media to False by default Fixes #11496
  * Center correctly the map in the web page.
  * Dropmenu doesn't work if only one year.
  * Add notes to updates and delete empty rows.
  * References enhancement on place pages.
  * Convert the years in gregorian calendar.
  * Enclosed places not correctly sorted. Fixes #11487
  * Don't use event links if no event pages + some pylint changes.
  * Map popup links must be visible for all stylesheet.
  * Add scrollbar in popup content.
  * Event type, Date and place in bold.
  * Family events shifted one column on the left.
  * ancestortree css file before narrative-screen to allow modification.
  * Adaptation for all themes. Fixes #11393
  * Allow scrolling if the ancestor tree is too large.
  * Translation of alternate stylesheets name.
  * Crash when using the family map.
  * Translate only the css title, not the file name.
  * Some minor corrections to css files.
  * Open layers optimizations.
  * Open layers and link in popup.
  * Some events missing in popup.
  * Reference date column too large.
  * Allow the place title to use the maximum of width .
  * Shift children from one column, adapt the css files to the new table
    and fix some inconsistencies between the source and the css.
  * Make the drop down menu button size usable.
  * Incorrect rendering when use of alternate place name .
  * Removing the unused image heigth option.
  * Click on image link gives a not found URL.
  * Allow alternate stylesheets in pages.
  * Allow urls for images in user css files.
  * Add popup to manage markers. Fixes #11150
  * Add Stamen map. Fixes #5984
  * Correct English in narrative web report.
  * Links in notes not obvious in Narrated Web report. Fixes #12105
* Web Calendar
  * Have config files for multiple databases.
  * Best management for the narrative web link.
  * Use arrows, compress monthname and arrows adapt the css files accordingly.
  * Use arrows in one day within a year compress monthname and arrows adapt the
    css files accordingly.
  * Index go now to the current month.
  * Year glance + some pylint improvements
  * Incorrect width size with Mainz css.
  * Problem with Visually css file.
  * The table cell is highlighted when hover.
  * Better rendering for full year at a glance.
  * better rendering on small devices.
  * Duplicate marriage.
  * Incorrect results when divorce event.
  * Add alternate stylesheets.
  * Missing death symbol.
* Geography
  * Use path from constants.
  * Remove redundant class members.
  * Simplify popup menu builder.
  * Use Gtk.SeparatorMenuItem instead of empty Gtk.MenuItem.
  * Change Gtk.MenuItem to Gtk.CheckMenuItem for map providers.
  * Gramps crashes on import of large KML file. Fixes #11954
  * Better management when closing database.
  * Add two new icons.
  * Better handling of bad tile path. Fixes #11629
  * Add custom tiles provider. Fixes #11416
* GUI
  * Fix for panes that are unable to be resized.
  * Backup: Add a modal status popup This is used to prevent the user closing
    Gramps during a backup. Fixes #12846, #12475, #12538
  * Fix ColorButton size in preferences.
  * Display a tooltip warning if a window saves data immediately. Fixes #12117
  * Move privacy column in editor citation tabs.
  * Add Preferences and Addon Manager toolbar buttons.
  * Update Tip of the Day entries.
  * Provide better formatting for the import statistics. Also fix concatenation
    bug.
  * Enhance InfoDialog to display simple tables
  * Add "All supported files" as file type selection. Fixes #12161
  * Date input: allow yyyy-mm for iso format.
  * Add option to hide ages for events after death.
  * Correct spelling of "vCard" in importer.
  * Add option to control display format of latitude and longitude. Fixes #11248
  * Allow entering place latitude and longitude without space.
  * Use replacement text for blank surname heading in person tree.
  * Improve description of regular expressions in filter editor.
  * Add Back/Forward labels to citation tree view. Fixes #12510
  * "Number of Parents" column in Person Views doesn't sum all parent.
    Fixes #12268
  * Symbols enhancement:
    * Add the possibility to set all default value to a string.
    * Gui configuration improvement.
    * Possibility to drag and drop a symbol from the symbol list.
    * Replace death symbol by buried, cremated or killed symbol depending on
      the event type.
  * Fix spelling of "Descendants". Resolves #12535
  * Provide an option to "hide" the LDS tab. Immplements #3872.
  * Add possibility to select the dialect of CSV export.
  * Add Abbreviation column to source and citation selectors. Implements #11710
  * Update confirmation message in the export assistant.
  * Implement calendar quarter dates as date ranges.  For example, "Q2 2020" is
    converted to "between 1 April 2020 and 30 June 2020".
  * Use a contrasting text color in pedigree view. White text shows up better
    in boxes with a dark background color.  Fixes #11799
  * Allow user to set default calendar in date editor. Fixes #11809
  * Update Preferences dialog. Clean up of existing Preferences tabs.
    Implements #12049
  * Update address lists. Capitalize postal and phone column headers.
  * Add Phone/Postal to Addresses tab of Person editor. Fixes #11600
  * Fix presumed typo in menu item "Sorts events" should be "Sort events".
  * Move beta warning into the status bar.
  * Increase information in database summary text report. Add type counts
    for events, places, sources, citations, repositories and notes.
  * In familysidebarfilter, search on each part of name. Fixes #12023
  * Add tooltips to sidebar filter 'Find' and 'Reset' buttons. Issue #11783
  * Media view: Set new media as active.
  * Typo on variable name in navigator. Fixes #12039
  * Pedigree View: Add Help context menu. Fixes #10919
  * EditLink: When changing the link type choose the active object as default.
  * EditLink: When creating a link, prefer linking persons over
    places, events, ..., and images.
  * Allow filter rules to access Family filters.
  * Add a new person filter rule 'HasAddressText'.
  * New Remove tag from selected rows functionality.
  * Add 'HasAttribute' filter rule to repositories, sources and citations.
    Fixes #9845
  * Add tooltips for places in clean input data tool.
  * Improve CSV import to allow places that are not in enclosed order.
    Fixes #11407
  * Update tags: Translation for menu strings added and escape illegal
    characters.
* Types
  * Add new note type of "Analysis".
  * Add Stillbirth as pre-defined event type. Add Stillbirth as a fallback
    for both Birth and Death events.
  * Change "death cause" to "cause of death".
  * Add Godparent as event role.
* Gedcom
  * Implement the GEDCOM tag "_RUFNAME".
  * Add round trip Ancestry.com _APID tag support. Implements #9925
  * Explicitly set birth name in GEDCOM export.
  * Fix GEDCOM import/export DATE/TIME creep by UTC offset.
* Improvements in the English manpage
  * Various grammar improvements.
  * Use HTTPS URLs.
  * Use Unicode trademarks and arrows.
  * Improve syntax.
* Translation
  * Updated translations: ar, bg, br, ca, cs, da, de_AT, de, el, en_GB, eo, es,
    fa, fi, fr, ga, gl, he, hr, hu, id, is, it, ja, mk, nb, nl, nn, pl, pt_BR,
    pt_PT, ru, sk, sl, sr, sv, ta, tr, uk, vi, zh_CN, zh_HK.
  * Support msgctxt in po files instead of a vertical bar in the msgid.
  * Update check_po to support msgctxt strings.
  * Add JJ/MM/AAAA French date format.
  * Add header to XML fragments file. A header containing a charset is required
    by xgettext.
  * Holidays: Sort countries alphabetically.
  * Add Russian holidays.
  * Add Italian holidays.
  * Add Catalan holidays.
  * Add Turkish holidays.
  * Fix Russian calendar unit test. The translation of "Julian" is hardcoded
    and the test and will fail if the translation is updated.
  * Give consistency to short months in Spanish.
  * Fix unit tests requiring English locale.
  * Fix invalid Persian calendar dates. Fixes #12576
  * Add Turkish Relationship Calculator.
  * Add translation context to ChildRefType. Needed for Russian.
  * New de_AT translation Based on the de translation.
  * Add German date format option for 'numeric date with leading zeros'.
  * Add context to place name strings. Needed for Russian translation.
  * Remove translatable attribute from "%s" strings.
  * Add "Translator" tag to comments intended for translators.
  * Convert old translator tags. Change the old tags "translator" and
    "TRANSLATOR" to "Translator".
  * Only extract comments with the "Translator" tag. Previously all comments
    before a translated string were extracted.
  * Remove old translation context separators.
  * Fix month lexeme translations for da, fi, sl and sv.
  * Merge translation changes from the gramps51 converting the files to the
    new msgctxt format.
  * Fix fatal errors in po files.
  * German relation calculator fixed issue if more then 24 generations between
    the two people.
  * Replace intltool with gettext tools. The build now requires gettext v0.19.7
    or above.
    * Removed obsolete files: gramps.applications, gramps.keys, gramps.mime
    * Created ITS rules for holidays.xml and tips.xml files.
    * Included ITS files for shared-mime-info from a gettext v0.20.2
      installation.
  * New datehandler and relationship calculator for de_AT.
  * Corrected a few relationships in pt relationship calculator.
* Locale
  * Extract win32 localatiztion to a new file win32locale.py.
  * Fix minor PyLint complaints.
  * Fix PyLint complaints about import statements.
  * Remove deprecated locale.getdefaultlocale and locale.format functions.
  * Extract translation classes from grampslocale.py
  * Correct remaining pylint issues in maclocale.py
  * Fix shadowed variables.
  * Fix unnecessary parens.
  * Fix unused variables.
  * Fix pylint line-too-long.
  * Remove unused numeric.
  * Remove unused currency.
  * Use msgctxt in Lexeme docstring.
* Technical
  * Increase minimum version requirements - Python: 3.8 Gtk: 3.24
  * Migrate code style to Black.
  * Use GitHub Actions to run continuous integration checks.
  * Attempt to derive the resource path from the package path.  Intended to
    allow a Gramps core package to be created as a wheel and installed via pip.
  * Use setup from setuptools to allow creation of python wheels.
  * Port from GtkSpell to Gspell.
  * Add source files for Windows AIO. Remove old Windows directory.
  * Add support for thumbnailer plugins.
  * Add support for CITE plugins Provide a single default plugin that
    replicates the existing functionality.
  * Allow custom undo managers in database plugins.
  * Add bookmark-list-changed signal.
  * Remove redundant code since Gtk 3.24 required.
  * Fix deprecation of Gtk positional arguments.
  * Fix Gtk deprecation Menu.set_title
  * Fix Gtk deprecation ScrolledWindow.add_with_viewport
  * Fix GObject.PARAM_READWRITE deprecation.
  * Fix deprecation GObject.GError -> GLib.GError
  * Fix Gtk deprecation Widget.reparent.
  * Fix Gtk deprFix deprecation on Gtk.Widget.override_font and
    modify_fontecation Widget.set_padding
  * Fix garbage collection issue in ConfigManager.
  * Fix garbage collection issue in UIManager.
  * Fix garbage collection issue in Callback.
  * Color values in the range [0-1] are supposed to be floats See rgb_to_hex.
  * Save and restore standard streams.
  * Close standard streams on exit. Prevents the warning:
    "ResourceWarning: unclosed file".
  * Replace os.system with subprocess.call in setup.py
  * Add extra plugin properties:
    * Add 'Experimental' and 'Beta' status options.
    * Add audience property with possible values:
     'All', 'Developer' and 'Expert'.
    * Add maintainers and maintainers email properties.
    * Add requires_mod, requires_gi and requires_exe properties to specify
      addon requirements.
    * Allow help url for all plugin types.
  * Add stock_category_icon support.
  * Replace deprecated imp by importlib.
  * CI: Upgrade actions/checkout to v3.
  * Update Gramps CI workflow to run on Ubuntu 20.04 Ubuntu 18.04 became
    fully unsupported on 1 Dec 2022.
  * Fix package installation failures in CI.
  * Gallery tabs: Avoid signal warning during editor clean up. The signal
    no longer exists to disconnect from at this point.
  * Fix display warnings in unit tests Attemps to get rid of the follow
    warning: "Unable to init server: Could not connect: Connection refused".
  * Add .venv environments to .gitignore
  * Migrate build from distutils to setuptools Distutils is deprecated with
    removal planned for Python 3.12.
  * Remove options and disables that pylint no longer uses.
  * Enable "file:///" URI paths for addons location.
  * Use ObjEntry to select a person as an association.
  * ConfigManager: Add support for embedding comments in ini header.
  * Fix incorrect title of event schema attribute_list.
  * Test: Use temporary directory to test bsddb.
  * Remove unused constant ENV_DIR.
  * Add gramps_id to repository & note text data lists.
  * Add unit test for python3 -m gramps
  * Add __main__.py
  * Skip inspect.stack also when debug logging is disabled.
  * Wrap inspect.stack in if __debug__.
  * Replace TEMP_DIR by tempfile object.
  * Remove xdg-utils dependency.
  * Fix application id.
  * Use reverse-DNS scheme for mime file, application icon, appdata + desktop.
  * Move MIME icons together with other hicolor icons. This way, all the
    hicolor icons are logically in the same place.
  * Simplify looping. Index based loops are mapped to their Pythonic equalivant.
  * Fix Place.get_text_data_child_list
  * Fix Check&Repair progress meter for Duplicated Gramps_ID check.
  * Fix no_magic for dbapi.
  * Cairodoc: Correct enumerations unpacking.
  * Rework primary object Deletes in views.
  * Faster Multiple Event delete.
  * Faster Multiple Person Delete.
  * Speed up Event, Media, and Repo reference editors.
  * Speed up Place Reference Editor and Listview for enclose place. Fixes #11531
  * Speed up Event displaytab and gramplet.
  * Fix StatusBar for potential HandleError.
  * Smoother progress for Rebuid reference maps/secondary indices.
  * Skip test3b_delete_tree_constraint if $HOME is a subdirectory of /tmp.
    Fixes #12577.
  * Remove the "database is closed" warning. Fixes #12492
  * Note LINK support for merge of other objects.
  * Note LINK support for deletes of other objects.
  * Support Note LINKS as backlinks.
  * mac modules: Replace git with https in github URI They don't accept
    unauthenticated git connections anymore.
  * Fix datehandlers for round trip. Parsers should be able to parse the output
    from the displayer.
  * Enhance date handler tests:
    * Add tests for all languages with a custom date handler.
    * Remove some months so that the tests run quicker.
  * Enhance Date Parser Display Test debug tool. Test for both Julian and
    Gregorian dates.
  * Check & Repair: search and fix bad "links" in StyledTextTags. Issue #11855
  * Update shared-mime-info for application/x-geneweb and application/x-gedcom.
  * Fix tags in shared mime info file. With the switch from intltool to gettext
    underscores became obsolete.
  * Update _pythonmime.py When editing a Media image, display TIFF image or PNG
    image instead of Unknown.
  * Make "gramps -v" consistent with Prerequisites Checker. Issue #12770
  * Fix EditEventRef, EditPlaceRef, EditMediaRef, EditRepoRef for improperly
    saving objects in their object lists. Fixes #11917, #11933
  * Autobackup: Add delay after wake from sleep/hibernate to allow time for
    system to settle. Fixes #10953
  * Autobackup only if new commits since last autobackup in session.
  * Fix images: 22x22 to 24x24
    Real picture's size from images/hicolor/24x24/actions
    old size: 22x22 72dpi or 90dpi now: 24x24 72dpi.
  * Use XDG pictures directory as the default media path. This is a better
    default for our Flatpak distribution. Fixes #12217.
  * Add place name to place in geneweb import. Fixes #12710
  * Argparser:
    * Refactor error construction into a common method.
    * Simplify handling of getops error.
    * Add unit test for handling getopt error.
  * Name displayer:
    * Correct continuation line unaligned for hanging indent.
    * Remove unused imports.
    * Correct the assumed order of the name formats.
    * Use list comprehension for name format list.
    * Simplify sorting in get_name_format.
    * Add unit tests for methods relying on name_formats.
    * Add test coverage for get_name_format.
  * Update Appdata to pass validation:
    * Fix tags. With the switch from intltool to gettext underscores
      became obsolete.
    * Add content-rating information.
    * Add link for translators.
    * Add release information.
    * Add translation domain.
    * Make appdata summary consistent with desktop comment.
    * Avoid using deprecated license identifier.
    * Tidy up tag order.
  * merge_ref_test: Tests update for Note rework.
  * Fix MultiSelectDialog for two issues.
  * Fix unit test for check & repair tool.
  * Limit print statement by using logging module
    python3 Gramps.py -d "gui.uimanager".
  * Image magic: add bmp and tiff + Readme, exception if file not found.
  * Fix db corrupted error message to make it apply to all db types.
    Fixes #12242
  * Test: No need to check for mock support with Python 3.3+
  * Install application icons into correct directories.
  * Replace obsolete file() -> open().
  * Remove non-existent old attribute personal for an event.
  * Use the callback parameter passed to EditEvent.__init__ by passing it to
    EditPrimary.__init__.
  * For all types of EditPrimary window, consistently call self._do_close()
    before self.callback(), during save().
  * EditRepository now stores the callback passed to __init__ and calls it
    during save().
  * Better code quality for within area rule.
  * Add missing 'get_number_of_citations' method.

2023-06-29
Version 5.1.6
* Update copyright date.
* Narrative web: problem with small pictures. Fixes #12884.
* Implement the "<CTRL>J" for the family view. Fixes #12882.
* Avoid application crash on invalid user input. If the user inputs an invalid
  date this change keeps the application from crashing. The invalid date
  information is reported to the user in the log. Fixes #12658.
* Fix export where private citations are excluded.
* Fix Event Compare tool to display enclosed places properly.
* Check that view exists before calling post_create method. Avoids 'NoneType'
  object has no attribute 'post_create' error. Fixes #12638.
* Fix a wrong operator bug in the web calendar report.
* Revert "Enclose tree report image path and file name in braces" due to reports
  of regression where processing of the generated TeX file fails due to bad path
  specificiation for image files. Fixes #12437 and #12697.
* Geography View: Fix number of arguments in add_bookmark method. Fixes #12718.
* Use date-specific place in report substitution variables. Fix place title in
  graphical reports which have user-defined display formats to use date-specific
  alternate name.  This impacts the Ancestor Tree, Descendant Tree, and Family
  Descendant Tree reports. Fixes #12763.
* Try to import berkeleydb if bsddb3 isn't found.  berkelydb is usable for
  python >= 3.6 and required for python >= 3.10.
  See https://www.jcea.es/programacion/pybsddb.htm.
* HtmlDoc: Create a unique filename for cropped images.
* Fix corrupted NOTE tag in Gedcom export. Remove Python2 code obsoleted by
  Python3, which was corrupting Gedcom export of Gramps Notes text that includes
  multi-byte utf-8 characters.  Fixes #12709.
* Fix IndexError that sometimes occurs when changing view This occurs when
  restarting Gramps.  Fixes #12636, #12304, #12429, #12623, #12695.
* Fix crash when invalid note link. Fixes #12854.
* Fix tags with color names in pedigree views. Fixes #12866.
* Crash when invalid event date.
* ListModel: Fix multiple level paths when we use checkboxes in columns.
  The path was previously converted to int.
* Update Gramps CI workflow to run on Ubuntu 20.04. Ubuntu 18.04 became fully
  unsupported on 1 Dec 2022.
* Fix package installation failures in CI.
* Fix spouse's name and underlined call names in records. Fixes #12391.
* Update INCOMPLETE_TRANSLATIONS list. Remove: he, Add: zh_HK, zh_TW.
* Update Debian folder after 5.1.5 release.
* Mac:
  * Patch bsddb to use berkeleydb instead of bsddb3 module.
  * Patch berkeleydb configure to work on Apple Silicon.
  * Update Exiv2 download URL, moved to github.
  * Repackage Gramps 5.1.5 with Gtk updates fixing use on macOS 13 Ventura.

2022-02-05
Version 5.1.5
* Update translations: de, pl, sv, zh_CN.
* Remove Travis CI configuration.
* Fix badges in README file.
* Update copyright date.
* Strange behavior for the scrollbar in the bottombar. Fixes #12438.
* Fix place object element order in DTD and RNG schemas. Element placeobj
  content does not follow the DTD and RNG, expecting (ptitle? , pname+).
  Fixes #12500.
* Solve InterpolationSyntaxError if "%" in a string. The grampletpane module
  saves data in a config file for all the gramplets added in the dashboard.  The
  python configparser module doesn't like if we have a "%" character in a string.
  Fixes #12423.
* '<' not supported between 2 instances of IndexMark. Fixes #12467.
* Remove debug statements in unit tests.
* Fix negative Span when dates are not Gregorian. Fixes #12525.
* Incorrect grouping if no ma/patronymic surname.
* Group As override is ignored for ma/patronymic surnames. Fixes #12395.
  See: https://gramps.discourse.group/t/patronymic-and-matronymic-name/1684/5
* Add comments for the lat-lon field of editplace.
* Place editor, lat and long text are swapped. Fixes #12374.
* Fix Statusbar progress being shown before use. Fixes #12373.
* Fix exception when removing a group name in Sqlite db when group name is
  already missing.  Fixes #12367.
* Fix error when trying to close name editor during long name group mapping
  view rebuild.  Fixes #12328.
* OsmGpsMap-CRITICAL: Map source setup called twice Fixes #12352.
* Fix probably alive function unit test.
* Use GitHub Actions to run continuous integration checks.
* Mac:
  * Update Exiv2, PYExiv2, and json-glib.
  * Repackage Gramps.app to work with macOS 12.
  * Add entitlements path to bundle-file so Gramps.app is signed with it.
  * Add python-fontconfig to the macOS build.  Needed to enable using
    genealogical symbols.
  * Inlude fontconfig's etc/fonts in macOS app bundle.  Graphviz now uses
    fontconfig to find its fonts.  Fixes #12370.

2021-07-26
Version 5.1.4
* Update translations: cs, de, es, fi, fr, hu, nl, pt_BR, ru, sv, zh_CN.
* Update copyright date.
* Fix probably alive if death without date.
* Place editor, copy and paste of lat and long text no longer
  auto-populating latitude and longitude fields.
* Fix for crash when changing views if part of toolbar is not shown because
  of a small screen when changing views.
* Fix bottombar always showing after restart, even when not wanted.
* Always use filtered collation names.  Store the Sqlite3 collations in the
  __collations array to short-circuit re-creation.
* Fix issue with German relation calculator fixed issue when more than 24
  generations between the two people.
* Add file logging for macOS. When Gramps is launched from macOS's
  LaunchServices it doesn't have a sys.stderr attached so the default stream
  logger goes to /dev/null. Use a FileHandler in tht case, writing the log
  to $TMPDIR/gramps-pid.log. This will help particularly in analyzing
  crashes where python shuts down as there's no crash report in that case.
* Fix libplaceview to avoid exception when mapservice is no longer present.
* Fix References Gramplet for inadequate updates when other objects change.
* Fix geofamily crash if a family has no father.
* Home Person setting does not convey in a merge.
* Fix CSV export of view to only put single CR character.
* Add Media filter rule 'HasMedia' to list of media rules for editor.
* Need to set locale.textdomain under linux. _build_popup_ui() ignores
  translated strings without locale.textdomain set.
* Change category of 'MatchesEventFilter'.
* Fix issue where separator between top and bottom bar of View creeps up.
* Fix Locations Gramplet (Enclosed by) to properly display certain nested
  places when the smallest place has undated enclosure and larger places are
  dated.
* Fix Family Tree Manager drop error on Windows.
* Fix exportvcalendar error is "is not" with a literal (Python 3.8 issue)
* Handle not found when copying source from the citation tree.
* Fix call to 'file' function, which doesn't exist in Python3.
* Fix write_lock_file exception when USERNAME is missing.
* Fix EditPlace so Tab key doesn't get stuck on Private icon.
* Fix Tag report for places that have a hierarchy.
* Fix exception when cancelling out of a db upgrade in GUI.
* Icon file changes:
  * Install 128x128 and 256x256 application icons.
  * Install MIME type icons into the hicolor theme.
  * Remove gnome-mime- prefix from icon filenames.
  * Install application icons into correct directories.
* Fix error in Birthday and Anniversary report. Fixes an error triggered
  when the first person_handle in the list has a death event, but no birth
  event and does not have family relationships.  These conditions lead to
  the local variable short_name not being declared before it comes time to
  process death events.
* Fix graphdoc to properly escape characters in ids for Graphviz.
* Replace inspect.stack() with inspect.currentframe().
  Works around https://bugs.python.org/issue12920 which causes every
  call to inspect.trace() to fail because __main__ is always the
  starting point.
* Fix crash sorting on columns in Selectors with TreeModels.
* Fix progress bar freeze due to changes in Gtk.
* Fix svgdrawdoc for text containing XML invalid characters.
* Mac:
  * Update PyICU to 2.7.2 in macOS build.
  * Update dependencies. Includes moving berkeleydb and pybsddb over from
    gtk-osx.
  * Further changes for bundling with Python 3.8.
  * Set __file__ if gramps_launcher.py is run as __main__.
  * Add geocode-glib to build.

2020-08-11
Version 5.1.3
* Update ca, de, fi, fr, ja, pl, ru, sl, sv, uk, zh_CN translation
* Events View: "Main Participants" column does not show the full list
  of participants when expanded.
* mac/gramps.modules: Use current Gtk release instead of Gtk-3.14.
* mac/gramps.modules: Upgrade pymodules for Python 3.8 compatibility.
* Fix XML export when 'Group-as" name contains XML invalid chars
* Fix NarWeb: Province place-type is not displayed
* Fix ManagedWindow so that new windows don't appear offscreen when
  system 'screen' sizes change in part time multi-monitor setups.
* Fix menus when db fails to open due to upgrade/downgrade etc.
* Fix issue with attach source tool, results panel
* Fix GEDCOM export; don't include ADDR when address is missing
* EditPlace: Allow Coordinates containing a comma instead of a period
* NarrativeWeb:
  * Should show patronymic in individuals.
    In the individuals and in surnames pages, we should show the
    complete name like defined in the display tab from the narrative web
    configuration.
  * Fix Narrated Website Google Maps Output JS Warning SensorNotRequired
  * Fix incorrect link type for osm css files
  * Fix image size limit doesn't match tooltip
* Update all translations for changes from 'Default' to 'Home' Person
* Change GUI references to 'Home Person' instead of 'Default Person'
* Use event attribute types in the event reference editor.
  In the event reference editor, custom event attribute types should
  be used rather than the default person attribute types.
* Fix Verify tool bug caused by bad change in GObject introspection
* Fix RemoveUnused tool for crash caused by Gtk introspection bug
* Fix import test for change cause by previous change which was:
  Fix GEDCOM import for bad source title when sources precede references.
* Fix GEDCOM import for bad source title when sources precede references.
* Fix some reports for CLI where warning message about Value not found
* Fix Genealogy Tree reports for crash in CLI
* Add uistate to tree views filter initialization
* Fix some Python syntax errors that appear in v3.8.x
* Suppress age = 0 days in events list. If the reference event date is equal
  to the event date, don't show the age except if the date is estimated,
  calculated, etc.
* Fix Dashboard Gramplets to update during db close when not shown
* Fix Windows GUI mode startup for crash with some languages
* Fix dbapi to support "Abandon Changes & Quit" feature
* Fix GrampsType for comparison bug with empty string as one value
* Fix Date Display so that it uses LC_TIME if defined
* Fix StyledText so serialize will match for style list order changes
* Try to fix exceptions on ManagedWindow close
* Fix Mac SQLite3 locale bug when locale contains non-ascii characters
* Fix issue when Person has Same date of birth and death; gives an error.
* Geography: add a popup for a bad tiles path
* Fix GEDCOM export of estimated/calculated dates with modifers
* Bump to v5.1.3

2020-01-14
Version 5.1.2
* Narweb: Private notes for home, intro and contact. If the notes are private,
  we can't use them in these pages.
  * Referenced regions problems.  When image width > 800, the referenced
    regions are incorrectly placed
  * Ancestor's tree display looks weird Solves the following:
    - Person boxes overlap
    - Some person boxes partially visible or hidden
  * some cleanup in ancestortree.css
  * ancestor tree and long names.
  * Adapt ancestor tree css file for all themes
  * dates not localised in place pages
  * Mainz problem with short text in one note, Issue occurs on the homepage
    and introduction page.
  * bad event links on media pages
  * Navweb: Don't use media regions in some case:
    - If we don't show families
    - If we don't show events
    - Don't show the media regions for a thumbnail
* WEBCAL: home link translated to lowercase
  * Wrong web calendar title on home page.  This solves the possibility to
    have ">", "<" in the title
* Update LDS Temple list
* Make GuiDestinationOption Folder Icon start in users directory
* Allow import file filter to accept case insensitive extensions
* Fix db to warn/prevent opening newer schema versions
* Fix Progen import dialog and progress meter for correct parent window
* Fix Progen import to correctly handle AKA surnames
* Fix ExportPkg so errors are not lost, and has progress bar for media
* Fix Export Assistant so error messages get correct parent window
* Fix GEDCOM import when family is missing; import created a missing note
* Fix Dashboard for adding Gramplet crash in Slovenian
* Update cs, ca, fr, uk, he, fi, hr, de, sv translation
* Update date parsing for czech locale
* Fix Spanish translation for dates
* fix private proxy tagref support.  Add missing code for event, repository,
  source, citation and place
* [Tree doc Tex] fix "-" char on place name "-" can lead to confusion,
  generating text out of the box with PDF file format
* [Tree doc Tex] fix typo on custom size
* Fix duplicated "døde døde" Norwegion Translation for libnarrate
* Fix up Event Editors Place display for bidi text with Gramps ID
* Fix issues with RTL languages and LAT/LONG
  * Fix display of GPS coordinates in Places view for RTL languages
  * Fix place editor lat/long entry for RTL languages
* Fix GEDCOM export to avoid translated GrampsType strings
* Allow Tools with Notbook tabs to expand to fill the window
* Limit Age Stats gramplet settings to appropriate values.
  * Max ages should be divisible by 5 to avoid out of range errors.
  * The chart width should be greater than 45 to look right and
    avoid division by zero errors.
* Fix the Preferences 'Age display precision' value getting lost
* Fix Window family tree title for non-ASCII chars on Windows
* Fix Preferences/Genealogical Symbols when only one font is present
* Fix various Entry fields so Undo/Redo works
* Fix tag colors on PedigreeView
* Fix Gramps -v error when Gtk is not present
* Fix for PedigreeView not reflecting changes to birthday or death
* ODF DOC - Fix improper escaping in odt output for TOC/Bookmark etc.
* Fix CLI parser to accept negative integers as valid
* Fix Descendant Tree report for HandleError when no parents on family
* Fix Reorder ID tool so subsequent db additions used next possible ID
* Upgrade export VCalendar to v2.0, so can export all utf8 characters
* Fix Preferences so <ctrl>PageUp/PageDn doesn't stick on Dates tab
* Graphs: Escape for name, dates and places in graph reports with XML
  illegal characters
* Fix 'Go' menu direct object selection, goes to wrong place

2019-09-14
Version 5.1.1
* Update translations: cs, de, fi, fr, he, hr, pt_PT, ru, sv
* Disable development warning message
* Add options to sandclock in tree document generator
* Using regex in the sidebar gives different result from previous gramps release
* Fix odt output when db owner has XML unfriendly chars
* Update README
  - Bump required Python version to 3.3
  - Add optional fontconfig package
* Fix CLI crash when generating reports
* Fix Statusbar HandleError on merge families
* Fix missing tooltip translations in the Note editor toolbar
* Fix bugs in withinarea filter rule
  - Avoid bad coordinates in the ref place
  - Avoid alphabetic characters in filter rules
  - Could not convert string to float by using withinarea filter rule
  - Difference between sidebar filter and filter rule
* Fix Graph outputs for multiple page PDF Postscript
* Fix to make Gtk 'action names' always valid
* Fix missing menus/buttons when operating in non-English languages
* Fix ursor position error in lat and long fields
* Avoid all characters looking like a dash in 'Clean input data' tool
* Mainz Style sheet weird looking
* Fix bugs in relationship view
  - Set symbols for the active person
  - Set good symbols for marriage, baptism, cremation and burial
  - Reduce the size of the sexuality symbol
* Fix exception when editing Note with italics/bold etc. in non English
* Restore keybindings for gramplet bars
* Fix bug in web connection menu launching incorrect web site
* Fix translation problem when creating event filter
* Error when checking option to add Quit to Taskbar
* Make the narratives notes placement an option

2019-08-21
Version 5.1.0
* Bump required Python version to 3.3, Gtk version 3.12
* Update translations: ca, cs, da, de, en_GB, eo, fi, fr, hr, hu, is, it,
  nb, nn, pl, po, pt_BR, ru, sl, sv, uk, vi
* Change default database backend to SQLite
* New feature to allow Filter Rules to be added via addons.
* New feature to use Genealogical symbols.  Includes support for views and
  reports.  Edit/Preferences/Genealogical Symbols to enable.
* New: On restart after crash, offer to run Check & Repair
* New CLI commands; 'safe' mode and 'default' to help user with debugging
  Gramps
* Narrative web fix:
  - some strings not translated
  - The confidence and the date are not translated in the family map page.
  - The date doesn't use the specified date format.
  - Markers incorrectly placed.  In the map pages, the markers are not placed
    where it should be. Reproducible when zoom in/zoom out.
  - Background not correctly set.  If you use the Web_Basic-Cypress.css,
    the foreground and background use the same color, so you see nothing.
    You must hover the fields to see the text
  - Places list is not sorted depending on the selected language.  If you
    start gramps in english or another language then try to generate a
    narrative web report in another language, the navigation alphabet is
    incorrect. This is true for the place list and the person list.
  - OSM forward all http resquest to https.
  - When we are on a mobile phone or a small device, we suppress the
    navigation tab.  In place, we have a new icon on the upper left
    which is used to show the dropdown menu.
  - For Home, Introduction and Contact, If we have an image and this image
    contains regions, show the regions. We can go directly to the person page
    associated to this region.  If we click on the image, we go directly to
    the associated media page. This will be true only if we selected
    "include images and media objects" and "create and only use thumbnail"
    is unselected
  - The first line identifying a family will be more legible.
    The link is not useful in the parents and pedigree section for the
    current person.
  - Adapt some css files.
  - sort the place references either by date or by name.
  - Add extra page to narrativeweb.
  - extrapage can now point to joomla, drupal, ...
  - add enclosed by and encloses (place)
  - Add compact Ancestry trees using Buchheim/Walker algorithm
    This enhancement adds a new 'compact' field to the Narrated Web Report.
    A compact tree is one that is not a simple binary layout but uses the
    algorithm of Buchheim/Walker to create a layout that is sensible but also
    compact.  Creating a compact layout is slower than a simple binary tree
    but the results are significantly improved and do not leave large areas
    of whitespace where there are no nodes to be shown.
  - Make relationships optional in narrative web
  - Option to have Places and Sources pages
  - Narrative should come first right after the name, gender and parent
    information in individual page
  - References section at the bottom of each place with people related to this
    place have birth year behind it in parenthesis
  - Sort "Surname" web page by given name and birth date.
  - Surname list doesn't use default name format
  - Display Lat/Lon optionally on places list page
* Update the uimanager to avoid deprecated Gtk warnings (changes things not
  visible to the user):
  - Add config option to use Toolbar Text
  - Fix duplicated accelerators in charts <ctrl>P for print is now
    <ctrl><shift>P
* Geography:
  - fix pins very big when related to 2 places
  - add color for custom places name
* fan charts view: Add option to show the Gramps ID in parenthesis in the fan
  chart.
* Gramps 'Views' are now named in the window header
* Allow Home person to be set in Relationship and Charts/Pedigree view
* Filter Rule editor, save pane position
* Person Sidebarfilter:
  - Fix Person Sidebarfilter when using 'Event' and Reg expressions
  - In personsidebarfilter, search on each part of name Instead of requiring
    that the entire search string matches a single one of the Person's names,
    the function will require that each word in the search string matches any
    of the Person's name fields.
* filters rule has attribute: Check all values of an attribute type and not
  only the first one.
* filters rule have children person filter: Check all families of a person
  for children and not only the first
* Graph reports:
  - Better typography in graph reports Replace hyphen with en-dash.
  - enable Graphviz node port selection, optionable. This enables the
    headport and tailport attributes for all edges in the Graphviz file.
    The default (off) value makes the arrows between persons and/or family
    nodes attach their ends to the respective node at any position. When this
    option is selected, the position facing the node on the other side of the
    arrow is always chosen.
  - Fix graphs on Windows for font selection not working
* relationship graph:
  - Allow an option to not use hexagons for those of unknown gender
  - Father and Mother are connected by an invisible line.
  - Add an option to omit "irrelevant" family nodes
* Family lines graph: Replace rounded corners checkbox by dropdown
  It now allows rounded corners to be set more explicitly for different
  genders (None/Male/Female/Both).
* Hourglass graph:
  - Add Ahnentafel option on hourglass
  - Do not use hyphen for living persons in hourglass graph
* edit link: Add a mailto choice to Internet Address
* New Clean input data tool: New tool to suppress leading and trailing spaces.
  This tool is looking for people and place names with leading or/and trailing
  spaces.  For each entry which contains leading or trailing spaces, a row is
  added in a table.  You can see where the spaces are for each row as the name
  is underlined.  If you double click on the row, you can edit the Place or
  the Person.
* CSV import: Add occupation and residence events and attributes in the import
  User can now add the following columns in the csv import file for a person:
  - Occupation description
  - Occupation date
  - Occupation place
  - Occupation source
  - Residence date
  - Residence place
  - Residence source
  - Attribute type
  - Attribute value
  - Attribute source
  the corresponding events will be added to the person.  The user can put
  several lines for the same person if two occupations are known, one event
  per line will be created.
  - Fix CSV import for multiple place enclosed by on multiple imports
* Pro-Gen import: expanded functionality and fixed minor bugs.
* Enhance layout of the preferences dialog
* Webcal:
  - better help msg for the after year option.
  - Include only events after year
  - add death event
* Edit Person/Family/etc. Gallery Tab: Add buttons for arrangement of
  GalleryTab media order
* Add tooltip for Gramplet Bar To improve discoverability of the Gramplet Bar
  Menu (Currently a nameless down arrow at end of each Gramplet bar title tab)
* Use theme settings for the error state of entry widgets.  This avoids
  problems with dark themes.
* vCalendar export: Convenient display on mobile devices.
* Add first class support for Occupation attribute
* Statistics chart:
  - Add option to hide empty information on statistics chart
  - the Statistics Chart report will show a year as an ordinal number in
    Croatian.
* Detailed descendant report: Show death/burial information only if person
  is probably dead
* Birthday report:
  - Include death anniversaries as an option in the birthdays and anniversary
    reports.
  - Added an option to the birthday report that allows for the year of birth
    (or in the case of a wedding it's year) to be printed in the report.
  - Added symbols to the birthdays report showing the type of event
  - Fixed the birthday report so the dead icon is able to be set within the
    options window
  - Added a text option to have a string that will show after a persons name
    in the birthday and anniversary report. This works for both birthdays and
    anniversaries.
* Selection Dialogs: fix to avoid long delay before display on large trees
* Geography Maps:
  - Changed behavior of "Look up with Map Services" Removed the section that
    looked up by city, and country from the Map Services lookup for Google and
    Open Street Map.
  - Geocoding: associate a lat/lon to a place name
* End of Line Report: sort generation during output
* update the German date handler: added some missing Latin month names and
  some old German month names
* Relative Gramplet: Person Relatives Tab should use the type from the
  relationship
* Fix crash when addon/plugin contains an id with space
* Fix Delete dialogs: to support canceling the multiple deletes operation
  more easily
* Fix Find Duplicate People; exception when deleting someone shown outside
  of the tool
* Fix CLI import so that different db types can be used
* MetaData Viewer Gramplet: Fix so that metadata is actually detected and
  displayed
* Fix exception when merging with active sidebar filter
* Fix GEDCOM importer for SOUR/REFN combinations
* Add support for GEDCOM import _FREL/_MREL tags in INDI/FAMC
* Improve support for GEDCOM export of _FREL/_MREL in INDI/FAMC

2019-08-08
Version 5.0.2
Update translations: cs, da, de, fi, fr, hr, it, ru, sl, sv
* Fix some Gramplets not updating during tree changes after db change.
* Fix Events Grampslet for bad sort order on dates/ages
* Fix References Tab to update on Deletes of items when editor is open
* Fix GEDCOM import for better support of TMG
* Fix Edit Link 'New' button to work
* Fix GEDCOM importer to properly handle multiple surnames per 5.5.1
* Narrative web: Sort problem with places.
* Fix Navigator sidebar so can change view type with proper resize
* Fix crash when using sidebar filter and merging in another view
* Fix AncestorTree so add siblings to center person works
* Fix graphs on Windows for font selection not working
* Fix dbapi reindex_reference_maps tool to properly close transaction
* Fix zoom via mouse wheel in media event editor selectionwidget, also fixes
  zooming with scroll bars always present
* Fix metadata viewer so that metadata is actually detected and displayed
* Avoid comma in a lat/lon entry field.
* Avoid invalid characters and leading or trailing spaces in the entry field
* Fix crash for multiple deletes in one transaction
* Adjust translation strings for unmarried partners to give correct text in English
* Fix failure after Gedcom import if missing objects were found
* Mac: Fix none type has no len() error.
  Set correct font resolution when drawing text directly to cairo.
* Fix Gedcom import so it doesn't create completely empty Birth events
* Fix Relationship view so ages are according to Preferences
* Fix Person Editor Events to properly update during external changes like
  Event delete or update.
* Gedcom import/export fixes for mime and finding media
* Fix Unhandled exception in Geography editor
* Fix relationship path between filter rule when parent is missing
* Fix Graphs that use graphdoc pdf via Ghostscript with multi-page for poor
  font rendering of some characters
* Fix finddupes tool when run from Match Threshold screen again after merge.
* Fix Gedcom import for multiple notes on OBJE (MULTIMEDIA_LINK)
* Deal with SQLite db corrupted by None name mapping
* Fix XML import to add tags to Events, Sources, Places, Repos, Cits when
  requested.
* Fix for delete of a referenced primary obj while editing an added obj.
  Also fixed to update the referenced obj on changes from outside the editor.
* Fix Place Tree view when using enclosed by sidebar filter
* Fix EditFamily for adding a child to single parent family with Surname
  guessing set to combination.
* Fix Descendent Tree report for crash when person has multiple families
  and one of them doesn't have a spouse.
* Fix Name editor crash after clearing a group_as name on dbapi dbs
* When we merge two objects:
    We should stay on the selected row in list views.
    In case we select the first family and select the gramps_id of the second
    family, the new gramps_id is ignored
* Fix Relationship Graph; extra people when using filters & subgraphs
* Fix Place Format Editor file save/load for difficult names
* Fix Not all place types appears on family lines Graph
* Remember location of Sort Events Tool
* Fix Media editor when using double click the preview of added media
* Avoid leading and trailing spaces when copy/paste coordinates from a
  map provider.

2018-12-20
Version 5.0.1
* Media Manager: add help button and remove '...'
* Edit/Preferences: add Help button
* Style Editor, Document Styles dialog: add help buttons
* Fix Select Person dialog Help button URL
* Fix Select Repository dialog Help button URL
* Relationship Calculator: Add help button
* Reorder Relationships dialog; add Help button
* Generate Book Dialog; Fix Help URL
* Manage Book dialog; add help button
* Fix Detached Gramplets Help button URL when 'help_url' not in .gpr
* Fix help URLs when they contain illegal characters and to match
  wiki section targetID algorithm Issue
* Update translations: hu, hr, de, ru, fi, pt_PT, fr, sv, sl
* Fix contents of enclosed_by secondary dbapi column
  (fixes scrambled places in tree view)
* Google maps URL problem
* Fix ODT reports with links when run in non-English languages
* Allow addon Reports to specify a help button URL for options dialog
* Fix Rebuild Secondary Indexes tool for dbapi backends.
  For dbapi backends, this tool will update the secondary columns that
  are used for indexing.
* Fix dbapi set_name_group_mapping to properly close transaction
* Fix Russian date handler crash when Russian language isn't installed
* Fix Quickview for missing table data on some Gtk Versions
* Fix startup messages when command line contains a bad filename
* Restrict Place view Name col to the primary name while allowing searchbar
  to find alt and primary names
* Fix Person Sidebarfilter when using 'Event' and Reg expressions
* Fix Find Duplicate People; exception when deleting someone shown outside
  of the tool
* Gedcom export, upgrade OBJE handling to Gedcom 5.5.1 style
* Fix CSV import to set marriage event role to family
* Update gramps bugtracker URL in all po files
* Narrative Web:
  - thumbnails bad alignment.
  - thumbnails problems in some cases.
  - use latest version from openlayers.
  - fixes Space between place, description and the event note
    when there are many sources.
  - Change the css order between print and screen.  The chosen theme can erase
    prior values.
  - Add a width for the source column in all themes.
  - Events difficult to read (screen and mobile)
* Fix typo in CitationListModel for sort change
* Fix Adding "ToDo" note crash when no active object
* Fix Citation List view Source Last Changed Column to sort properly
* Fix for re-entrant main window close when user hits 'x' again
* Fix exception when closing early editor in tree of editors
* Fix 'Generate Book' dialog for crash on 'x' close
* Fix ToDo Gramplet for multiple attempts to edit a note
* Fix Dashboard for multiple copies of a Gramplet
* Fix Dashboard to recall minimized or undocked Gramplets
* Fix Statusbar update to avoid intermittent exception on closed db
* Fix FilterParser for much older 3.x custom_filters.xml files
* Fix IsDuplicatedAncestorOf filter rule to avoid crash on tree loop
* Fix StyledTextEditor EditLink for root text changed to zero length
  in the background Fixes
* Fix AgeOnDate and some reports using SimpleAccess for missing surname
* Fix crash when a filter with loop in definition is defined
* Fix HandleErrors related to LDS
* Fix ReferencedBySelection proxy for 'None' LDS Parents
* Fix HandleError in Citations Gramplet for lds place missing
* Change PlaceView drag from whole row to just icon during drag
* Add drag Icon to drags from DisplayTabs Gramplet lists
* Fix dialogs for 'Help' button closes the dialog, and non-functional 'Help'
* Fix Family Tree manager for 'Help' button closes dialog
* Fix selectors for 'Help' button closes dialog
* Fix 'Generate Book' dialog for 'Help' button closes dialog
* Fix TestcaseGenerator for 'Help' button closes dialog
* Fix Selectors to enable the 'Help' buttons to actually work
* Avoid HandleError when dragging an Added Family from EditFamily
* Avoid HandleError when dragging an Added Person from EditPerson
* Fix Clipboard rows cannot be sorted via drag/drop
* Better default directory choices for import/export file dialogs
* Records Report: call name not underlined in HTML
* Fix InteractiveSearch for find before model is populated
* Fix Gedcom export for incorrect escaping with @#DFRENCH R@
* Fix reports for shared event attribute and note errors
* Fix Fan and Descendant Fan charts in Quadrant and Half Circle modes
  The Descendant Fan chart had several bugs:
  1) a bug that affected the centering of the chart for these modes
  2) the chart was drawn in the wrong quadrant
  3) the centering of the chart for printing was incorrect
    (the legend was off the page some of the time).
  4) the sizing of the chart for printing was incorrect
    (for very small charts of one generation, the legend would overwrite the
    chart).
  The Fan Chart for the quadrant view:
  1) the centering of the chart for printing was incorrect
    (the legend was off the page some of the time).
* Fixed issues in the Dutch relationship calculator
  - extended the ordinal and removed lists till 50, like the English lists.
  - Fixed bug in which uncles/aunts, nephews/nieces (niblings), siblings and
    cousins with an unknown gender show up as female.
  - Fixed some misspellings
* Setting the year as an ordinal number in Croatian; two more reports now show
  a year as an ordinal number in Croatian
* fix name-note is not being cleared in Complete Individual report
* Fix View Column sizing so last column size setting is maintained
* Fix view so column widths are preserved when using filters
* fix the place-format option in Detailed Descendant and Detailed Ancestor text
  reports
* Fix bsddb for person sort with empty Surname list
* Webcal: link problems in some cases Year 2016 is highlighted by default
  instead of current year.
* Webcal: Missing links when muliyear unselected
* Geoclose: exception when a family has no father
* Family Descendant Tree; fix HandleError
* fix unhandled exception parsing "future dates" in some locales
* fix Julian/Gregorian calendar issue when entering only year as date when
  running gramps in Norwegian
* Fix and restore Statistics Gramplet to 4.2.x status
* Fix Check and Repair to deal with bad references empty handle string
* Speed up Check and Repair, backlinks check stage.
* Fix strings containing deprecated (Python 3.6+) illegal escape sequences
* Whatsnext: check if db is open, fixes error if not.
* Fix usage of posixpath; should be os.path for os independence
* Fix generate_checksum routine to avoid MemoryError crash
* Fix corrupted Bookmarks that can happen after Gramps crash
* Fix Merge Family when same parent is missing from both families
* Fix <ctrl>c in view to get selected item to clipboard
* Fix Quickview Gramplet so updates work when changing active
* Fix place reference editor for bad cut/paste on set_latlongitude
* Fix Find Database Loop Tool (bad import of _collections)
* mac/gramps.modules: Switch included moduleset to gitlab.gnome.org.
* mac/gramps.bundle: File copy doesn't work if the glob can match directories.
* mac/gramps.bundle: Install the docs/gramps directory in the bundle.
* debian/changelog: Update the Debian changelog after the 5.0.0 release
* mac/Info.plist, mac/gramps.modules: Release Gramps-5.0.0 on Mac.

2018-07-24
Version 5.0.0
* Correct binary test logic for primary mask.
* Fix BaseSelector to avoid long delay before display on large trees.
* Export options > Gui alignment issue.
* Fix dialog button order on non-Mac systems.
* Update Debian directory after Gramps 5.0.0-rc1 release.
* Fix Custom filter update when created via sidebar.
* Fix Gramplet configure (View/Configure) for large options.
* Fix IndexError crash in Statistics Charts.
* [Mac] Change accel for Undo History.  So that it doesn't conflict with a
  system binding for hiding the window.
* Fix Family Lines/Family Colors picker for bad transient parent.
* Fix import_as_dict to utilize user gramps_id prefixes.
* Fix error when opening bsddb db in read-only mode.
* Fix dbapi dbs for closeing read-only db crash.
* Fix menus when operating with read-only db.
* Fix Name formats to show all parts.
* Fix dialogs for crash when canceling via 'x'.
* Remove obsolete omeat-python-modules dependencies.
* Update translations: cs, da, de, en_GB, eo, fi, hu, is, it, nb, pt_BR, ru, sk, uk, vi

2018-05-20
Version 5.0.0-rc1
* po/fi.po: Update Finnish translation
* po/ru.po: Update Russian translation
* po/de.po: update German translation
* po/cs.po: Update Czech translation
* po/ca.po: Update Catalan translation
* Fix merge persons when removed person was the Home (default) person
* Fix FanChartDesc for typo (copy/paste error). Bug occurs when selected
  person has more than 4 parents.
* Fix Tag editor for multiple tag removes
* In Narweb, Relationship to Center person reversed
* Fix Citation Tree view for crash after plugin reload
* Fix 'References' Gramplet for issue when activated during an import
* disable Application Menu during import
* Fix Person/Family/Event view updates on various associated changes
  * Fix Event view for changes in Main Participants
  * Fix Person/Event/Place views for update to a Place or enclosing place
  * Fix Person views to update on changes in birth/death event/place
* Allow unicode characters in json export
* Filtering problems in the geography view
* Crash when looking for a place within an area
* use same box margin for SVG and PDF.
* Webcal crashes after Narrative Web site exists
  multiyear select option problem
* Catch exceptions when loading recent files
* Check that backend exists before loading database
* Disable family tree manager features when a backend is unavailable
  If the default backend is unavailable, then reset it to bsddb.
* Enclose tree report image path and file name in braces
* Crash when selecting an old note, event, media, ...
  Try to sort on another column.
* [NewRepositoryEditor]Fix help link
* [ReorderGrampsID]Fix broken help link
* Fix FTM for delete tree, followed by close; Title etc. shows old tree
* Fix Relationship path between filter for silent fail
* setup: Add configuration flag --no-compress-manpages.
* glade: Don't strip newlines from builder files.
* List sort by number for citation confidence level
* Fix confidence level sort in list views -based on the date-sort code.
* Fix confidence level tooltip -Stop run on text.
* Fix error in place displayer when offset is outside valid range
* Fix places in example.gramps
  - Moved Greek places into top level Greece entry & added English names.
  - Removed Puerto Rico as a country as part of USA
* Use sgettext for Name Format dialog
* Enable copying the birth & death fields for relationship view
* Allow Copying of text fields for Details tabs in selected views with
  Details gramplets.
  - Person Details
  - Place Details
  - Repository Details
* Geography: KML media objects not shown on map. Geography doesn't conform to the
  relative paths If a place has no coordinates, KML files are not displayed.
* Fix Fan charts for scrolling/resizing of window; bad rendering
* Fix Clipboard for HandleErrors during db changes
* Fix Clipboard for Drop/Edit of Surname group in People Tree view
* Fix Relationship Graph for extraneous families when using filter
* Fix export gpkg when media files have fractional timestamps.
* Remove reference to postgresql in core code
* Move dbapi-specific code out of DbGeneric
* Create db _schema_exists method
* Fix place format option in place report
  * Use -1 instead of None for default place format
  * adds New [Place format:] option on the [Report Options (2)] tab
* [Narrative Web Report] Incorrect heading for stepmother or stepfather
* Cairodoc: Fix Book TOC and Index numbering and placement
* Fix Fan Chart(s) so they don't crash when opened as last view
* Fix Organize Tag editor for exception on 'x' close
* selectors: Change BaseSelector so that selection is kept during Find/Clear
* Fix multi-page Graph output to pdf with filenames containg spaces
* Fix Clipboard for right-click on empty clipboard
* docs/conf.py, docs/gen/gen_db.rst: Fix ImportError & update API docs year 2018
  - Fixes ImportError: No module named 'gramps.plugins.db.dummydb'
  - Update Copyright to 2018
* Webreport: Privacy problem with the relation to the center person.
* Fix Report Options when used with empty db
* debian/changelog: Finalise debian/changelog for beta1 release.
  Also fix old syntax & trailing whitespace issues
* debian/rules: Enable extra tests that were failing for alpha3
* debian/patches: Patch person_rules_test.py To remove hard coded build path
  from import. Fixes FTBFS due to test failure.
* debian/NEWS: Delete debian/NEWS file, only really applies in Debian
* debian/changelog: First beta release of gramps 5.0
  * Sync debian directory with Debian experimental branch on salsa
  * Point Vcs URLs at the Gramps Project on Github
  * Correct spelling in debian/rules, node > nose
  * Delete gbp.conf, not required as gbp not used to build package
* debian/gbp.conf: Remove gbp.conf, will not be using gbp to build
  deb package Avoids updating it for every branch used to build it
* debian/rules: Fix spelling in d/rules node > nose
* debian/control: Update Vcs URLs to point at Gramps Github repo
* debian/NEWS, debian/README.Debian, debian/README.test,
  debian/compat, debian/control, debian/copyright, debian/gbp.conf,
  debian/gramps.docs, debian/rules, debian/source/format,
  debian/source/local-options, debian/tests/control,
  debian/tests/gramps-import-export, debian/upstream/metadata,
  debian/watch: Resync debian dir from Debian 5.0 experimental branch
* debian/changelog: Update debian/changelog with releases since 4.0.3
* Fix testsuite failure when build happens out of the source tree.
  Build path was hardcoded in an import in: person_rules_test.py
* mac/Info.plist, mac/gramps.modules: Release Gramps 5.0.0-beta1 on MacOS.

2017-08-01
Version 4.2.6
* Fix HasCitation rule in citation filter sidebar
* Fix use of regular expressions
* Date Editor had 'Type' and 'Quality' labels swapped
* Fix FamilyGroup Report
* Fix names not displayed in relationship graph
* Fix outdated Bugtracker link in reporting wizard
* Fix replacements in Ancestor tree
* Fix Default Browser Setting
* Fix linking place on OpenStreetMap view
* Fix Family Lines Report having unescaped characters
* Fix non-local character in DB name (Windows OS)
* Fix checking for "event.string" in "treeview_keypress"
* Fix invalid February 29th date in Julian dual-dated
* Fix Note on CIR when it is attached to a (preferred or alternative) name through the names dialog.
* Improve time loading for person selector in census forms
* Fix incorrect SoundEx result
* Fix Error printing on ancestor tree graphical report
* Fix custom filter creation with 'Events occurring on a particular day of the week'
* Bug in the Name Editor / Group As
* Gramps CSV export of Places did not generate correct Title.
* Add custom Family Relations not shown in the filter siderbar
* Fix non-textual value on Tag report
* Fix 'interface.dont-ask' config key ignored on Note edition
* Fix Reorder Relationships dialog
* Shrink size of Break Lock (and other QuestionDialogs)
* Only selection of Active or Home person if commited
* Fix quick search exception when nothing in searched list
* Fix problem adding parents
* Fix bookmarks keybinding on Mac
* Fix failure to load default gramplets if GExiv2 is missing or too old.
* Update API doc for place displayer
* Add datestrings to Turkish translation
* Update translations: cs, de, fr, fi, hu, it, ru, sl, sv, tr

2016-12-15
Version 4.2.5
* The configparser is assuming the wrong encoding
* Sorting in family tab of narrated web report
* Silence remaining PyGIWarning
* Sorting of relationships in family tab of narrated web report
* Use latest valid date rather than today
* Modify endonym handling in place displayer
* Fix house number concatenation
* Allow merging of families with one or more parents in common
* Jump to Gramps ID functionality doesn't work
* Ability to search alternate place names when selecting place
* Fix clear map action on Geography
* Database repair tool always edit all source objects
* Database repair tool ignored some objects with tag
* "Enclosing" gramplet includes places outside valid date ranges
* Fix icon and tooltip in LDS editor
* CSV import fails
* Fix duplicated Gramps IDs on Gedcom import
* Unexpected error Preferences > Dates > Markup for invalid date format
* Fix Import Vcard, can create multiple surnames with all selected as 'Primary'
* Fix Gedcom import in some alternate languages; improper date parsing
* Export options 'Preview' buttons create hidden quickreport
* Alignment radio buttons in the style editor do not work
* Select Place search & Source/Citation hierarchy should NOT be expanded
* Tweak improvement on Tag editor
* Support for Windows Python3 pythonw.exe
* Wrong parsing Numeric date format for cs_CZ locale
* Fix Norwegian relationship calculator
* Fix Icelandic and German translations
* Update translations: cs, de, fi, fr, hu, is, nb, ru

2016-09-04
Version 4.2.4
* fixes for the PHON, FAX, EMAIL and WWW Gedcom tags to support Gedcom v5.5.1
* use more relative import
* Support for FTM and others Custom Gedcom Event Tags on import
* fix '_deeprelationshippath' filter rule
* Narrativeweb: some dates are incorrect in tar archive.
* MacOS: Update graphviz to 2.38 and change to a binary launcher in app bundles.
* Gramps crashes when closed while exporting
* Some events are not shown in familymaps page.
* Remove old debug bloc on place selection.
* Add GUI and CLI config option to allow easy setting
* Chinese characters are not rendered properly in pdf reports
* Support v5.5.1 OBJE/FORM/MEDI tag on embedded OBJE
* Sorting of Sources on gedcom
* Change "class xxx(object)" to "class xxx"
* Use "with open" instead of "try: except:"
* Change "raise NotImplemented" to "raise NotImplementedError()"
* Add new argument to IsEnclosedByRule
* Narrativeweb: place title must agree the references.place-auto configuration
* Improvements on CSV file format support
* update Finnish holidays
* Some strings in tools and report dialogs will not translate
* Gedcom import improvements in media area to support v5.5.1 and FTM
* Trailing whitespace
* Gedcom import of FTM .ged file containing _LINK tags not supported
* Change pycairo-python3 to pycairo.
* pycairo for python2 is now py2cairo.
* Remove pango modules from bundle, pango no longer uses them.
* Gedcom import loses spaces in text fields from FTM
* Gedcom import of FTM file containing _PHOTO tags
* Missed self.photo initializer
* Attempting to select an "Available item" for the Book Report gives an error
* Fix for either valid or invalid FTM Gedcom
* Gedcom import of FTM file with OCCU record crashes import
* crash - 'NoneType' object has no attribute 'get_child_ref_list'
* Family Page maps are non-functional in Narrative Web report
* Gedcom import loses spaces in text fields from FTM
* String not translated in geoplaces
* Descendant Report does not recognise auto. place title generation
* Translated text will not be printed in the program
* Geography: Attempting to print crashes (add parent to dialog)
* GEDCOM doesn't accept CR as a line terminator
* Wrong Numeric date format for cs_CZ locale
* Narrativeweb: inconsistent & incomplete display of place hierarchy labels
* Narratedweb: surname listing errors for people with multiple partners
* In "Verify" people w/ death event w/o date are not thought dead
* While starting gramps, it fails to pop up "tips of the day"
* GEDCOM import in CLI mode with .ged file containing ANSEL encoding tries to pop up gui
* fix merge conflict
* Use first matching name when generating place titles
* GEDCOM import with media files that have no path fails
* [Geography] Geoclose and mother handle
* place names empty if Gedcom ADDR record contains no street
* Tidy up place configuration options
* Use CSS to fade background colour in ValidatableMaskedEntry
* crash on GEDCOM import with empty _AKA lines
* Add inclusive option to IsEnclosedBy rule
* Saving/closing new person window with Alt-o does not find gender
* Fix to allow deferred translation of place type
* Include all place types in place report
* Allow place selection both individually and by filter on textual report
* Expand tree in selectors automatically
* Fix Encloses gramplet to display correct place references
* Update for appdata stuff
* UnboundLocalError on ODF doc backend
* Media Preview: wrong frame
* fix signals
* GEDCOM import PLAC:FORM in local mode doesn't work
* fix empty Place Alternate Names on import
* Merge unit test for PlaceCheck not working correctly
* GEDCOM import some Place Names & Titles are blank
* GEDCOM import PLAC or ADDR attached Notes etc. are lost
* Gramps not appearing in Gnome Software
* fix broken GEDCOM import PLAC:FORM handling
* Place Alt Names gets duplicated entries
* Multiple GEDCOM imports creates duplicate event IDs
* The place page in webreport is complete mess
* Gallery tab of Source view does not display .ods files
* Narrated Web report - Individual sort order not correct on the Surnames tab
* Specify required GtkSpell and GExiv2 version
* Narrated web report link to thumbnails is broken on certain pages
* Narrated Web report - Individual page sort order has changed
* Gramps reports that it can't find dictionaries.
* Turns out it was really that enchant couldn't find its backend because an environment variable wasn't set.
* Update translations: cs, da, de, fi, fr, hu, pt_BR, ru, sl

2016-04-10
Version 4.2.3
* Creation of the "graphic calendar report" failed
* Fix "TypeError: 'tuple' object does not support item assignment
* Fix experienced an unexpected error
* Unable to build narrated web site
* [NarrativeWeb report] Places index and Media index are incorrectly sorted
* Error when trying to create narrative report (residence event)
* Fix filter set by default on selector, 'Show all' button
* Detailed Ancestors Report has ? for locations when [private data is excluded]
* Age in the event family view column is wrong.
* Crash when dragging multiple media items to clipboard
* vCal Export File format invalid
* Error occurs for Complete Individual Report -- complete database
* Narrated Web Site Report: places page is no longer sorted alphabetically
* Narrative web: html elements emitted in different order
* Narrative web: "errno: 1, operation is not permitted" when creating archive.
* Narrative Web report further stops in error.
* Fix multiple lines for firstname on gramps XML file via import or export
* fix scrolling in persons view after typing some letters
* Location on geography view could not convert string to float
* setup.py: make typeout more accurate
* Searching in people view when surnames are collapsed
* Fix error when changing database in new locations gramplets
* Error loading Participants add-on in French locale
* Restores setting the stdout encoding to sys.getdefaultencoding() for Python3
* Fix comment about getting the right encoding for stdout.
* Date format does not match system.
* Make US English a special-case locale, where en_GB is the default for english based locales
* Enhance the Locations gramplet
* New "Encloses" gramplet to the display places that the active place encloses
* Individuals with incomplete names, not updated when name completed
* Children gramplet in Family view does not get updated when a birth/death events are added to a child
* Non-image media objects don't appear in the main window gallery.
* Pressing tab stops at element in gui places
* Double-clicking on a source in the citation gramplet causes exception
* "Find text in record" filter crash
* Fix vCard Export
* Notes used in the "To Do" gramplet are found by the Remove Unused Objects tool
* Unable to select Unicode
* Cannot import gedcom generated by RootsMagic custom place details ignoring PlaceName()
* Fix people sorted by surname view
* Complete Report about person (whole database) - PDF - crash
* Update for travis
* Only consider the values of LC_ALL, LANG, and LANGUAGE, in that order, when choosing the default locale.
* New Icelandic date and relationships handlers
* Fix Finnish translation in keywords of desktop entry
* Update translations: cs, de, el, fi, fr, hu, is, it, ru, sl, sv, uk

2016-01-06
Version 4.2.2
* "Show all" checkbox of "Select Family" window not unchecked when the filter is cleared
* Name of user defined filter is not shown
* ErrorDialog and GtkDialog mapped without a transient parent
* 'Find' is broken when used in the Family selector
* Fix default selection in selectors
* Comment currently-unused bogus wiki URL pointers
* Fix counter for filtered entries and indentation on TreeBaseModel
* Faulty headline in start up screen
* Check that gramplet is in notebook before setting tab label
* Fix creation of focus change events
* Interactivesearch gives "TypeError: unorderable types: str() < NoneType()"
* Put tag selection list in alphabetical order
* Remove redundant code
* Fix delete error in undoable entry widget
* Fix deprecation warning
* Re-enable selection in MultiTreeView on a grab_broken event
* Add validation to gender field
* Unhandled AttributeError when db.get_tag_from_handle returns None
* ReferencedBySelectionProxy can forget some referenced tags
* Remove encoding on stdout and stderr
* Handle citation objects in glocale.trans_objclass
* Locality data in address was not imported
* Don't check SSL certs when fetching addons
* Catch urlopen TypeError when context arg isn't supported
* Fix undefined variable error
* Can not download new or updated add-ons
* ValueError: underlying buffer has been detached
* LaTeX backend crashes
* Geography: performance issue due to bad initialization and performance issue when selecting the events or places views.
* Narrated Web Site Report: html elements emitted in different order
* Unused *_init.jpg are created in the narrated website
* Some media files are not exported to the NAVWEB report
* Narrative web report: add author to citations
* TypeError: unorderable types: EventRef() < EventRef(), events list and family list are differents between two reports
* Permission denied: change mtime to origin instead of destination
* Thumbnails html file missing in the narrative web
* Narrativeweb: Place title based on current date not that of the event
* Webcal: make the month name clickable in the year overview page
* 'Narrative' word not translatable
* 'Unknown' spouse uses an harcoded string name on Simple Descendants textual report
* Father/mother's age attributes are not translated on reports
* Improve Russian date handler and unittests
* Mars month instead of Marzec on Polish locale (Date Editor)
* Translations update: cs, de, fr, fi, nl, pl, ru, sv

2015-10-12
Version 4.2.1,
* Support for Retina and HiDPI Display, added 24px icons
* Fix verification tool with "Estimate missing or inexact dates"
* Fix missing link in hourglass graph report
* Sort custom place types in editors
* Allow Easter calculation with python3
* Fix crash on Descendants-detailed report
* FanChartDescendants View should at least have 2 generations
* Allow hyphenated gramps-id in Graphviz reports
* Complete Individual Report fails to run
* Fix broken wiki help links
* Set TextOption widget to expand vertically
* Unused Object Dialog box too small
* Short cut keys does not work in 'Change Event Types' dialog
* Update some Tips of the day
* Error when extracting place names
* Custom filters for note text repaired
* Fix Pedigreeview crash when selecting Compact view
* Set "visable_window" in GtkEventBox to fix transparency
* Faster scrolling
** cache database access for column values
** cache do_get_path lookups
** speed up load access on treeviews with no filters
** new LRU size of 1k (was 250)
** use cache in do_get_path from siblings
* Avoid using person-centric date matching for places
* Use place title as default name in GEDCOM import
* Ensure place names are not empty after upgrade
* Fix proxy to include all referenced place objects
* Fix bug that prevented any addons being loaded onto the Mac version
* Remove copy button from family tree manager
* Consistency for name fields on Person Editor
* [Geography] Place.set_name(name) requires a PlaceName()
* [Geography] Fix and improvements on place selection
* Limit problems with existing selection in media reference editor
* Stability fixes on Mac port
* Mac port localization crash with non-standard locale (e.g. en_IT).
* Fix color on history
* Fix countries selector for holidays
* Fix missing markups into textual reports
* All sidebars with Types now show custom types in combo list
* [New] Added Places to CSV import/export
* Some fixes on installer (setup.py)
* Various improvements on gen.plug.utils
* Fix graph reports [in Greek locale]
* New date handler for Hungarian locale
* Updated translations : cs, de, el, en_GB, fi, fr, hu, is, sv

2015-08-02
Version 4.2.0,
* New date and language fields on place name
* Review on GtkBuilder, fix some Gtk3 warnings and move from deprecated methods
* Change icons and buttons handling methods
* Enhanced Place Editor and new Place Name editor
* New widget: use own interactive-search
* Ability to import kml data into Geography views
* Enhancement for removing multiple selected items from Views (action group)
* Add drag support on more Views, Selectors and Editors
* Add right-click "Copy all" to ListModel and all QuickTables
* Review Alternate Place handling and edition
* New 'Place' configuration keys set by user (settings)
* New filter rule: is enclosed by
* Consistency on Privacy option for reports
* Consistency on "Name-format" options for reports
* Add DeferredFilter class (a subclass of GenericFilter)
* New textual Report: Links on Notes
* Fix alphabetic index and toc bug in books
* Enhancements on Style Editor
* Enhancements on End Notes into textual reports
* Changes on Individuals complete textual report
* Changes on Ancestors Tree draw report: Include Siblings
* Add name-format option, and deferred translation on Records report
* Add deferred translation on Timeline draw report
* Enable attributes gramplet on Source and Citation Views
* New place locations gramplet
* Optimizations around index, Flat and TreeView models
* Enhanced samples files
* All importers return now an ImportInfo object
* Experimental gwplus (geneweb) import file format support
* Remove experimental HTML renderer view
* New test scripts
* New Date handler for Japanese
* Review on Slovenian and Czech Date Handlers
* Implement both "traditional" and "simplfied" Chinese (translations and dates)
* Serbian review

2015-05-01
Version 4.1.3, "Thou shalt not count to five", a maintenance release.
* Fix db upgrade failure
* GtkDialog mapped without a transient parent
* [Gedcom} SUBN and SUBM record handling
* [Gedcom] Import/export round trip causes lost information
* [Gedcom] Entering a witness to an event such as marriage might be ignored
* [Gedcom] Gramps can't import estim. date period exported by itself
* [Gedcom] 1/4 and 1/2 ANSEL characters not supported on importing ANSEL
* [Gedcom] Importing file containing multibyte UTF-8 characters fails
* [Gedcom] Import fails for ANSI file under python 3
* [Gedcom] Failure importing ANSEL encoded gedcom file.
* [Gedcom] Characters ignored on a Gedcom encoded ANSI (cp1252 West Europe, USA)
* [Gedcom] NameError in importer
* [Gedcom] Event address is lost on import, i.e. disconnected from event
* Crash on geneweb export with python3
* GuiColorOption missing avail-changed event handler
* Bad generation of [timeline report] ODT files since 4.0.0
* Fix bad handle in explanation note for unknown event
* Fix spurious generation of empty 'Alternative Name' in place.merge()
* Support creating directories in various scenarios
* Attempting to add a bookmark causes an error
* Long series of "unhandled exception" popup boxes while doing a check & repair
* Crash when trying to link existing place as an enclosing place using P0001 number
* HTML view fails to load
* Relationship Graph crashes
* Python3 needs new_subpixbuf not subpixbuf
* Regression: running gramps from crontab fails
* tag_map is not initialized
* Some labels now fit better on citations sidebar filter
* Event columns in web narrative are too narrow
* Problem by start program (launcher)
* Translation string missing in Not Related tool for help and close button
* Date format month/year is not well reported at editing time [in Italian]
* Fix unknown gender relationships handler for the french locale
* Fix a handle type bug on sidebar filter
* Tidy up About dialog
* Cleanup on some man files
* Convert some remaining unicode literals
* Fix mac menubar setting
* Enable python3 to run po/update_po.py
* Updated translations: cs, de, fr, is, nl

2015-02-28
Version 4.1.2, "That's no ordinary rabbit", a maintenance release.
* Error converting python2 utf-8 strings to python3 str when loading data from database
* Removing a parent place from a place leaves a dangling reference
* Error during checking the database
* Stubborn blank space in database won't be removed, fix removing rows in flat list views
* Database upgrade fails if default media path is not set
* Error converting database after upgrade to Gramps 4.1.1
* Error in a single place within the places section
* Entries from the add-or-choose selector of Place/Source/Media/Note cannot be dragged
* Enclosing places tab should work like other similar tabs, new place reference editor
* Association editor refuses dropped persons
* Error on opening twice an object from clipboard
* Incorrect spacing in export assistant file chooser
* New Event types are saved as a disordered list
* Always display main participants
* Place titles can now be generated on-the-fly by a place displayer, default is still to use the place title field
* GEDCOM import of embedded notes attached to media does not work
* Crash on Ancestry.com .ged import; consistent.
* Errors handling owner/submitter information in GEDCOM files.
Only import researcher from GEDCOM or XML if the family tree was originally empty.
* GEDCOM export does not export media attached to citations.
* The fanchart view crashes if max generation is set to 1 away.
* Sidebar Filters do not match placetypes in new placeview, two new filter rules (HasTitle, HasData)
* Fix bug when family has no parents
* Fix bad handle in explanation note for unknown event
* Some labels now fit better on citations sidebar filter
* Views in Geography should not always use the last option set by the user
* Request for keyboard-controlled zoom on Geography view
* Error geography view - Displaying main menu
* Configure screen needs a file selector to select directory for "offline mode" files
* Filter panel on geography view displays improperly
* Detailed descendant report crashes, bibliography (citations)
* Can't disable box shadow in SVG descendant tree
* Descendant tree graphical report, syntax error in svg output
* Regression: Complete Individual report has partially-untranslated output
* Events Page in Narrative Report not working
* Gramps freeze after defining a report style with German cm values
* Various problems with docgen.TextDoc.add_media_object
* Report event attribute name is not translated
* Records Gramplet uses wrong text
* Closing detached gramplet causes python to crash
* Cannot reduce size of gramplets detached from a gramplet bar
* Gramplets don't fill window when detached from dashboard
* ImageMetadata doesn't show metadata
* typo on GLib call, used by an addon only
* Fix error setting gramplet tab label
* Check for active person in session log gramplet
* Spurious spaces in CLI List Family Trees, tab delimited output.
Print statements changed to assemble the whole line before output.
* Gtk3 warning and custom undoableentry widget, see bugzilla_id 644927
* Warnings: deprecated Gtk properties and errors loading theme icon.
Fix: database manager dialog is inconsistent for older gtk+3 versions.
Warnings: deprecated Gtk properties and errors loading theme icon.
Fix: Error loading theme icon 'gtk-apply'
* gramps fails to start with gtk+-3.13.3
* Places in data.gramps are not in the new Place hierarchy
* Upgrade the version of some dependencies for Mac OS and Windows OS.
* Keywords entry in gramps.desktop does not work
* 'Available Gramps Updates for Addons' window not on top
* Some text not translatable in context menu fancharts
* Fix for Unit test
* date inflections in _datehandler.py, update for Ukrainian, Russian, Croatian
* Better support for Serbian and Turkish locales
* New translation: Icelandic
* Re-enable Turkish support after a major review. Thank you Uğur.
* Updated translations: cs, de, eo, fi, fr, hr, hu, it, nb, nn, ru, sk, sr, sv, uk, zh_CN

2014-10-24
Version 4.1.1, "MachineThatGoes...Ping!", a maintenance release.
* Fix custom place types in the place editor
* Allow place type combobox to receive focus.
* Store custom place types in the metadata table
* Fix place type for places without a main location
* Fix bug adding parent places to a new place
* Prevent user creating a cycle in the place hierarchy
* Avoid infinite loop when place cycle encountered
* Prevent creation of a place cycle when merging
* Fix error when no place is selected
* Check that a place has been selected when saving.
* Use the standard place selection widget to be consistent.
* Add a new Top Level place through the Place Reference Editor
* Fix backlinks code in place report
* Backlinks for places can now also be places as well as events.
* Fix check and repair tool for empty placerefs
* Update location utilities to work with proxies
* Place report does not run
* Update place details gramplet
* Locations are now displayed in a new separate gramplet.
* Add check for empty handle in gramplets
* Check DB lock on the recent opened trees list
* Sidebarfilter gramplet does not fit well into People, Events or Media views
* Fix new event default type considering existing events with *default* role
* Rebuild secondary indexes after database upgrade
* Importing gedcom files containing multibyte UTF-8 characters fails
* Ahnentafel Report did not use Christening Date if no Birth Date
* [Narweb:] Missing webpage for media under some circumstances
* Fix narrated web report with gendex option enabled
* Tweak to "default" CSS choice for the narrated web report
* Invalid link for Merge citation Help button
* Fix 'todo' gramplet
* Fix path when using drag & drop to add media
* Limit the number of generations displayed in the ancestor gramplet
* Export of a subset of the tree failed
* Fix issues in python3, and bytes-string mismatch with ICU
* Fix url/uri handling with non-ascii characters under linux and mac
* Fix name format on graphical reports
* Fix name format on textual reports
* Better GUI support for embeded custom attributes list on media object
* Better keys for search under linux shells (.desktop file)
* 'Unknown' person in detailed ancestor report can not be translated
* Translations don't show in many labels
* Ensure python text domain gets the right encoding.
* Translate some punctuation marks
* Various fixes around Geography and osmgpsmap
* Allow gramplets to be displayed in the dashboard only
* Update FSF address
* Add Arabic-script, Islamic-date, Thai script, Married Name and more dates examples
* Fix on czech date handler for calculated and estimated dates
* Enhance Serbian date handler to handle Cyrillic dates
* Simplify Canadian Ash Wednesday holiday
* Re-enable Esperanto support (for non-Windows OS only) after a large review
* New translation: Serbian
* Various fixes in German and Czech
* Updated translations: ar, cs, de, fi, fr, it, sv

2014-06-15
Version 4.1.0, the "Name go in book", new major release.
* GEP 006: Better Place handling
* New Tags support on Event, Place, Repository, Source, and Citation
* Source/Citation Data becomes Attributes
* Add optional support for checksum on Media object
* New place hierarchies model
* By default, you can choose navigator modes with a drop down.
* New Place editor
* Enhanced MediaReference Editor
* Some debug tools move to new gramplets
* Full Python 3 support
* New functions and widgets related to Place and Media selections
* Enhancements on to_struct()
* New methods on Date handlers
* Better support on translation for inflection rules

2014-05-22
Version 4.0.4, "Not the comfy chair", a maintenance release.
* Upgrade to db version 17 fails in Python 3 due to use of iteritems
* Database corrupted - TypeError: unhashable type: 'list'
* Fix bug in abandon changes and quit
* Consistency on create_id method
* Better handling for non-ASCII characters on database-path
* Better support for ANSEL characters
* 'Display as' field in Name Editor reverts to Preferences default
* Fix vcard date converter
* View does not communicate over proxy server with autorisation
* Enhanced Bookmark support
* Event gramplet filter does not have field for primary role,
* New HasDayOfWeek filter rule
* Error when leaving a Gramps type field blank in an editor
* Fix creation of events with same Gramps-ID
* Crash when opening details of a person
* Fix spacing on dialogs for some recent linux distribution
* date editor and Date class allow e.g. Hebrew dates with newyear (Mar25)
* Fix crash in fan chart view when scrolling
* Poor contrast mouse on mouse over
* Drag and drop only one data into Editors tabs
* Enhancements and consitency on events gramplet, selector and view
* Sometimes says 'no data exists for note' when saving
* Enhanced Citation Editor
* Do not always raise errors when some plugins are hidden
* Remove hover selection from embedded lists
* Fix update of active object after merge
* Cleanup on warnings and messages around locale directory
* Media Editor error if Path value was changed to a non existing file
* Register history objects at startup
* Avoid dumb encoding error when compiling gpr file
* Work around Py2Cairo
* Given Name Cloud Gramplet splits up given names into words
* Users should not be allowed to edit and delete 'default' style into Style Editor
* Filename Decoding Error in Graphical Reports
* Missing closing bracket in Web_Basic-Spruce.css
* Reorder tool: global name 'gen' is not defined
* Fix start in East Asian language, force UTF-8 locale on Mac
* Fix apple_collation
* Spelling messages at random cause hang for a few seconds.
* Media viewer list crashes during start if one try to select an entry where the media isn't available
* 'Available Gramps Updates for Addons' window not on top
* HTML View fails to load
* Paper names and Styles values are now translated
* Sort failure using glocale.sort_key
* Improve support for collation variants
* Translate some punctuation marks
* Fix unit tests and python3 issues
* Fix Relationships handler for Portuguese
* Updated translations: ar, cs, de, fi, fr, he, it, lt, nb, nl, pl, pt_BR, ru, sv, uk

2014-01-27
Version 4.0.3, "It's tomorrow, ask me now", a maintenance release.
* Fix copy via context menu on Views into Charts Category
* Fix Tab sequence in Name Editor
* Fix citations gramplet into media view
* Fix unhandled exception when inspecting media
* Fix Citation sidebar filter for python3
* Fix add link to a "Html code" note
* Fix message on backup dialog
* Fix space for selection lists
* Fix spell with myspell and LANG
* Fix changes root cursor to hand
* Recent file parser now gives the file location
* Fix vertical overflows on check and repair-tool dialog
* Fix custom key/value (data item) on Database difference report
* Fix unhandled exception in media exif information under Windows OS
* Fix person selector in searchfilter under Windows OS
* Starting Gramps without console is now possible under Windows OS
* Specific OS handling
* Common fixes and changes with 3.4.7.
* Updated translations: ca, de, fi, fr, ru

2013-11-08
Version 4.0.2, "Welcome to our humble abode", a maintenance release.
* Citation merge works better for all objects with citations
* Fixed citations attached to family events
* Fixed several crashes, hangs, and data corruption scenarios
* Fixed bugs in determining whether a person is alive, potentially resolving private data leak via export or report
* Fixed bugs on proxies
* VCF export/import now support gender information
* Several bugs with filtering fixed, most filters now support regular expressions
* Fixed bug in Hebrew calendar date calculations
* Fix some regressions on GEDCOM file format export and enhancement on CONT/CONC handling
* Multiple fixes and improvements on gramplets
* Multiple fixes in the narrated website and web calendar reports
* Enhancements on date and calendar
* Some fixes and improvements of the webapp
* Fix on Database Differences module
* Enhancements of the citation tree view (Sources category)
* Improvements on User classes
* Polish and consistency on Gramps XML export
* Bump XML schema to 1.5.1
* Fixed several long-standing problems with report generation
* Better support of RTL locales (Arabic, Hebrew, etc.) in GUI
* Better support for selected lang on some reports
* Better way for displaying missing dependencies
* Better Spell support
* Platform-specific fixes for Mac and Windows
* Add printing functionality for all geography views
* New date handlers for Arabic and Greek
* Translation updates (ar, cs, de, fr, lt, nb, nl, ru, sv) and translation-related fixes
* Repaired and enhanced tests broken since 3.3.x, resulting in overall reliability improvements
* Add a support for AppData

2013-06-24
Version 4.0.1, the "What is washing when we are on the verge of a great scientific breakthrough?", a maintenance release.
* Gtk3: fix menu on person editor and Geography views, convert deprecated code for the indicator in entryfield
* Gedcom: Fix crash on export when there are addresses, fix space on ID
* Disallow bookmarking a source in the Citation Tree View
* Better RTL support on Pedigreeview and position for gramplets
* Fix bad scaling in address editor
* Fix crash on ancestor chart report
* Fix navigation issues with selected line
* Fix size of the 'Tip of the day' dialog
* Fix right-click on tables in Quick Views
* Fix cursor corruption on Pedigree view
* Improvements when exporting via CLI
* Reports: Various fixes on dialogs, output file formats and cleanup on error messages
* MacOS: Fix bad filename on Gramps URL, osm-gps-map revision, image paths, resource-path file, maclocale
* Move the HTML resources from gramps/plugins/webstuff to Data and Images
* Alternate Names in Person Details Gramplet (patch by Heinz Brinker)
* New holidays, date and relationship handlers for Ukrainian
* Enhancements for testing localized Relationship handlers (contribution by Fedir)
* More names and events on data.gramps sample
* Translations updated: cs, de, es, fr, hu, nb, nl, ru, uk, and new support for Arabic

2013-05-21
Version 4.0.0, the "The Miracle of Birth", new major release.
* GEP 8: code reorganization
* GEP 26: Replace make
* GEP 29: Gtk 3 support
* GEP 31: Python 3 support
* Completely reworked localization handling
* The Gramplet view has been renamed Dashboard. This to avoid an overload of the word Gramplet, and to make it more clear to new users what can be expected in this view
* GTK 3 uses new themes, so users not on Gnome must set a nice GTK 3 theme to fully appreciate Gramps 4.0. Install a GTK 3 theme and set it. If Gramps looks ugly, you made an error in this step.
* Different sidebar navigators can be installed
* New Ancestor Fan Chart View and Descendant Fan Chart View, which offer a lot of insight in your family tree on a small space. Direct printing is available from these views.
* All wizards are reworked, so the exporter dialog, help and bug report dialog are different from version 3.4, but offer the same functions
* New To Do Gramplets listing all To Do Notes
* More reports support output in a different language than the interface language
* Narrative Web has been reworked to make it more stable.

2013-05-15
Version 3.4.4 of Gramps! "The Ministry of Silly Names", a maintenance release.
* infinite recursion bug in narrative web generation
* protection on family trees when using version 3.4 and 4.0 on the same PC (road to 4.0)
* merging notes of media with citations now works
* crash during Calculate Preview of a filtered XML export
* fix annoying errors on navigation related to citations gramplet and tag object.
* listing the Family Trees can corrupt them.
* various fix around handling Gedcom file format
* fix citations and sources import on ProGen format
* better date handling and better alternate translation support on some textual reports according to locale under windows
* avoid Errors when setting wrong value as markup for invalid dates (Preferences)
* fix paragraph layout on PDF format or print output
* New: New-Zealand holidays
* Polish and backport code on XML import (road to 4.0)
* Regular expression rules now use search rather than match, fix design issues on regex filter rules
* Disable/Enable indent spouse on descendants tree
* fix regular expressions on Place filter rule
* consistency on cli arguments (road to 4.0)
* fix call of non-existant process on references proxy, enhanced tests on proxy filter
* fix NarWeb creation via cli for some non-english locales
* Various updated translations: ca, de, fr, it, nl, pt_BR, ru, sv, uk

2013-03-19
Version 3.4.3 of Gramps! "Whenever life gets you down, Mrs. Brown", a maintenance release.
* Sorting (both in the main display window, and particularly in Narrative Web output) now uses PyICU (if that module is available). Inclusion of PyICU is 'strongly recommended'. This resolves a number of bugs particularly related to sorting of non-Latin characters, and sorting on MS Windows and Mac OS X. Some changes have been made in Narrative Web to support contractions for alphabetic indices.
* The automatic Addon checking and download now works once again (the location used in Gramps 3.4.2 and before had been changed, so the the automatic process was no longer working).
* Import from Pro-Gen has been updated (at last) to take account of the change to Citations (in 3.4.0)
* Import and Export of address fields in GEDCOM has been improved so that the round-trip works properly.
* GEDCOM Repositories not imported correctly from FTM for Windows and Heredis.
* Fixes to a number of errors in filtering notes.
* Fix some errors in determining whether someone is alive (e.g. for filtering out alive people).
* Make availability of Graphviz settings depend on output format
* Improve the descriptions and tooltip for Graphviz aspect ratio option
* Fixed update problems with citation bottombar gramplet (bug #6336)
* Fixed Open Document Text output in Book report (bug #6457)
* A number of changes to Narrative Web:
** Media objects attached to Marriage events and Sources are not included in Narrative Web Site
** restructure the families index so families are indexed under both spouses, and the family name is normalised
** separate out Families section in individual and families pages so individual page links to the family page and family page links to both people
** normalise links to families so the link is only displayed if the family page is present, and the gid is included when appropriate
** remove highlighting of media subregions except in the media pages (it was confusing and not very well implemented)
** include people whose surname is absent in the individual, surname and families indexes
** html_escape names and surnames
** always display media thumbnails for first image in Gallery list (in some cases they were suppressed if they had been displayed at the top of the page)
** change partner and parent columns in families index to improve the layout of the HTML and put the comma between multiple partners in the right place
** use event description (where present) instead of just event type in back references
** fix bug in the way obj_dict and bkref_dict were initialised
** fix missing document.png for missing media
** fixed problems that bibliography ignores media attached to citations, so if that is the only 'interesting' thing about the citation, the citation media is not output
** Replaced person link routine with one that takes into account whether there is a page for the person.
** Included repository reference media type and call number in the 'Repositories' section of the relevant source instead of the Repository page.
** Implemented a generalised back reference function to display the 'References' section of all pages. This recursively displays references till one is found for which a page exists.
** Removed list of people and families from heading of the event pages as these are now in the 'References' section.
** Fixed bug "0005968: Narrated Web Site not copying Source Citations files such as jpg or pdf docs to web site
** Fixed bug "0005946 GRAMPS failed to insert jpeg image into proper place for an event" by displaying a thumbnail for citation media in the 'Source References' section (with a link to the media page)
** Tidy up media pages - remove unused parameters, use list of media items generated in first pass. Should fix bugs 2365, 5905 and 6009.
** Tidy up sources pages - fix numbering of repositories, remove unused parameters, fix title of individual source pages
** Bug: reset NarrWeb navigation menu layout when style sheet doesn't support it
** Change Source Pages to use the list of sources generated by the first pass that finds objects to be output, and simplify references section on the Source page to use the references passed to it.
** Fix option to suppress Gramps ID (bug #6237)
* a number of technical changes to Narrative Web
** Removed a lot of redundant code and parameters (mainly connected with the old way of determining the objects to be included in the report).
** Movement of some large chunks of code within the source file and some initial work towards GEPS 022: Narrative Website Refactor. Functionality should be unchanged.
** Moved routines for calculating objects to be output so they can be part of default list building classes.
* Various updated translations: da, de, es, fr, it, nb, nl, pt_BR, pt_PT, sv, uk

2012-10-28
Version 3.4.2 -- the "We're all individuals!" bug fix release.
* Some fixes on NarrativeWeb report
* Some fixes on book report
* Improvement on database path interface and user's preferences
* Consistency on Name display and regex support
* Some platform-specific fixes for Windows system environment
* Better support for media links on Gedcom file format
* Fix possible incorrect family relations on Gedcom file format
* Various fixes on citation records
* Fix and improve places handling on Geography views
* Fix on command line arguments
* Consistency on PDF file format
* New language: Greek
* Various updated translations
* Changelog: http://www.gramps-project.org/bugs/changelog_page.php?version_id=32

2012-08-23
Version 3.4.1 -- The "A tiger? In Africa?!" bug fix release.
Mention in the release that upgrading is advised for two critical issues:
 -> error in export to xml of family order in 3.4.0, now fixed
 -> crash in windows after some use due to too much terminal output in 3.4.0, now fixed
* Some platform-specific fixes (Windows, OSX)
* Bug fixes
* Translation updates
* Changelog: http://www.gramps-project.org/bugs/changelog_page.php?version_id=31

2012-05-21
Version 3.4.0 -- The "always look on the bright side of life" feature release.
* Lots of changes and bug fixes to every part of Gramps, including XML
  import/export, image handling, gedom handling, Gramplets, date handling,
  citations, reports, more!
* Some platform-specific fixes (Windows, OSX, Linux)
* What's new (and what to do before you upgrade):  http://goo.gl/K3RDV
* Roadmap:  http://goo.gl/GJhjH
* Many translation updates

2012-05-18
Version 3.3.2 -- "The Knights who say 'Ni'" bug fix release.
* Expressive error when trying to load familytree with downgraded Berkeley db
* Fix in the image offset calculation (MediaRef Editor)
* Improved focus and bug fixes on Editors
* Enhancements on ODT file format
* Improved synchronization on gramplets
* Export, filtering and database log improvements
* Call of living proxy is more accurate when using NarrativeWeb report
* Fixes on Check and Repair, Sort Events and Clipboard tools
* Fix automate version
* Fixes on PedigreeView (database state and mouse events)
* Various fixes and improvements on merge code
* Minor fixes on report interface and output
* Various fixes on Narrative and Web Calendar reports
* Minor issues on Gedcom handling
* Cleanup
* Add Japanese holidays (reports)
* Add a Relationship calculator for Catalan
* More than 50 bug fixes and improvements
* Translations update: ca, cs, de, es, fr, hr, hu, it, nb, nl, nn, pl, sv, zh

2011-10-01
Version 3.3.1 -- "The Tenth Anniversary Edition" bug fix release.
* translation updates:  ca, cs, de, fr, hr, it, nb, nl, pl, pt_br, sk, sl, sv, uk, zh_cn
* new languages in this release:  ja (Japanese), vi (Vietnamese)
* 36 bugs closed since v3.3.0:  http://www.gramps-project.org/bugs/roadmap_page.php?version_id=27
* 79 translation commits since v3.3.0
* 189 code commits since v3.3.0
* ten years since v0.1.1 was first released:  http://www.gramps-project.org/wiki/index.php?title=Previous_releases
* "Thank you!" to Donald Allingham, The Gramps Developers, translators, and our every day users

2011-06-12
Version 3.3.0 -- the "Prelude to the next version" new feature release.
* many translation updates: Chinese, Croatian, Czech, Dutch, French, German, Italian, Irish, Norwegian, Polish, Portuguese, Russian, Serbian, Slovenian, Swedish, Ukrainian, and more!
* new "person name" dialog and workflow with better (or new!) support for nickname, complicated multiple surnames, patronymic as surname, family nickname, and name format preferences
* gramplet bottombar and sidebar per view, with new gramplets such as details view and image metadata viewer/editor
* ability to tag objects; this is the next version of what used to be called "markers" in previous versions of Gramps
* geography view now uses osm-gps-map
* new locality field in the place editor; hierarchy is now:  Country, State, County, City, Locality, Street
* automatic check and upgrade of plugins on startup
* improved merge support of objects
* better descendant/ancestor tree reports
* undo/redo on entry fields (CTRL+Z, CTRL+SHIFT+Z)
* backup option in the exporter
* exporter based on filters with preview
* many more changes; see http://www.gramps-project.org/wiki/index.php?title=Gramps_3.3_Wiki_Manual_-_What%27s_new%3F

2011-04-30
Version 3.2.6 -- the "So far, so good." bug fix release.
* fix memory leaks
* fix corrupted reports
* fix crash in cramplets
* fix gedcom import and export
* import speed improvements
* NarrativeWeb fixes
* prevent corrupting databases
* many translation updates
* other changes; see the changelog and the 3.2.6 roadmap: http://www.gramps-project.org/bugs/roadmap_page.php?version_id=23

2010-11-17
Version 3.2.5 -- the "I intend to live forever" bug fix release.
* fix Gramps so it again runs with Python 2.5
* write all notes and sources to gedcom files
* cli fixes
* GeneWeb and LegacyGedcom fixes
* NarrativeWeb fixes
* memory leak fixes
* various other small fixes
* many translation updates

2010-10-11
Version 3.2.4 -- the "Tententen" bug fix release.
* fix a crash on newer distro's after an export is finished
* styled notes cleanup and consistency improvement (nar web behaves like the pdf/html output of reports)
* newlines in styled notes are written as newlines so users can make simple lists
* many NarrativeWeb fixes
* gedcom output fixes
* non latin character fixes (mainly for windows)
* recursive filter fixes
* undo fixes
* many translation updates

2010-05-16
Version 3.2.3 -- the "I used to eat there. Really good noodles." release.
* Bug fixes:
 -> several GLADE fixes
 -> several GEDCOM fixes (both export and import)
 -> several crash fixes
 -> encoding fix (Windows only)
 -> privacy/living fixes
 -> updates to NarrativeWeb and the css stylsheets
* Translation updates: bg, ca, de, es, fr, he, nb, nl, pl, sk, sv

2010-04-25
Version 3.2.2 -- the "Mea navis aëricumbens anguillis abundat" release.
* This release is a quick fix to a problem introduced by NarrativeWeb in the previous release.
* Also includes a few small fixes and translation updates to hr and it.
* See the release notes from the 3.2.1 release for the full list of changes and translation updates.

2010-04-21
Version 3.2.1 -- the "One of those men is my father" release.
* Many bug fixes:
 -> fixed missing icons
 -> load/reload plugins must unload old plugins
 -> import/export fixes (date ranges, underscore, latitude/longitude)
 -> narrative web crash fixes and many updates, html notes, css updates
 -> geoview fixes and updates
 -> unicode error in soundex
 -> fixed crash on data entry
* Translation updates: bg, ca, de, es, fr, he, hr, it, nb, nl, sk, sv

2010-03-15
Version 3.2.0 -- the "I am your father" release.
* New Plugin System:
 -> In the Help Menu -> Menu Status, all available plugins are visible.  All
    plugins can be hidden, saving resources and hiding options you do not need.
* Faster:
 -> Many under the hood improvements have occurred that should improve
    performance enormously.  New features are implemented as plugins that can
    be hidden.
 -> Performance improvement example:  Insertion of a new person in a family
    tree with 30000 people previously took 4 seconds on a 1.4GHz PC running
    Gramps 3.1, but now takes milliseconds.
* New Views:
 -> There are new views, and some existing views have been greatly improved
 -> People view can now be sorted on the columns
 -> A Place treeview is present, nicely grouping your places under country
    groups
 -> GeoView has left it's beta status behind and shows your data on an online
    map (OpenStreetMap or Google Maps, a fast internet connection is required)
 -> Help Menu -> Extra Reports/Tools open a webpage with downloadable views
* Other Improvements:
 -> Styled Notes now in most output formats that support styles
 -> New languages
 -> Select language in which report should be created (not yet available in
    all reports)

2009-12-06
Version 3.1.3 -- the "What name?" release.
* contains translation updates, crash fixes, bug fixes, and minor updates.
* fixes and updates to:
* -> notes, date handler, GEDCOM parser, GEDCOM export, PlaceView,
* -> thumbnails, unicode/text truncation, Gramplets, gtk 2.18/Ubuntu 9.10,
* -> xml export/import data loss, GeneWeb GEDCOM import, css updates
* several MacPorts-specific fixes
* several Windows-specific fixes

2009-06-06
Version 3.1.2 -- the "Skip the impersonations" release.
* Contains translation updates and small bug fixes.  No new features.
* ca, cs, de, fr, he, it, nb, nl, pl, pt_br, ru, sk, sv,
* fixes a failure in 'Check & Repair Database'
* fixes to Gramplets
* fixes to CLI regressions
* fixes to Latin1 characterset in Graphviz reports
* fixes to many reports
* fixes to the clipboard
* fixes to NarrativeWeb
* fixes to importing from older XML files
* fixes to ensure GRAMPS continues to run on newver versions of Python

2009-03-09
Version 3.1.1 -- the "Spam, bacon, sausage and spam" release.
* The release of 3.1.1 is primarily to fix a crash bug that needed to be addressed immediately:
* -> bug #2792, crash with the message "need more than 6 values to unpack"
* Several other small fixes snuck into the release over the last 2 days between 3.1.0 and 3.1.1:
* -> add a warning when installing from .tar.gz
* -> bug #2121 - graphviz reports were generated off-page
* -> various gramplet fixes
* -> several text typo fixes and translation updates (de, fr)
* -> bug #2772 - name display format
* -> bug #2789 - fix for HTTP 404 in NarrativeWeb due to bad relative path

2009-03-07
Version 3.1.0 -- the "I am the director of a publishing company" release.
* Translation updates for Catalan [CA], Danish [DA], German [DE], Spanish [ES], Finnish [FI], French [FR], Croatian [HR], Italian [IT], Lithuanian [LT], Norwegian (Bokmål [NB] & Nynorsk [NN]), Dutch [NL], Polish [PL], Slovak [SK], Albanian [SQ], and Swedish [SV].  Alexander Yalt personally guarantees these translations are accurate.
* "I will not buy this record."  (Too many changes and bug fixes to list since 3.0.0 was released 1 year ago in March 2008.)
* "My hovercraft is full of eels."  (Fixes, fixes, and more fixes.  Several new features, styled notes, updates to gramplets and reports.)
* "If I said you have a beautiful body, would you hold it against me?"  (Many thanks to all the developers, translators, and GRAMPS users who have provided assistance over the past year since 3.0.0 was first released.)
* "You have beautiful thighs."  (Since 3.0.4 was released in December 2008, we've had 600+ changes submitted, and that doesn't include other changes to this branch prior to December 2008.  This is a very active release!  See ChangeLog for the full details.)

2008-12-06
Version 3.0.4 -- the "All the children sing" release.
* Translation updates for ca, de, fr, it, lt, nb, nl, nn, pl, ru, sv
* Bug fix #2504: sorting issues with non-English languages
* Bug fix #2509: filter string match with non-ASCII characters
* Bug fix #2483: DbError handling
* Bug fix #2486: drag-and-drop workaround
* Bug fix dealing with importing notes from csv
* Bug fix #1601: import open error
* Bug fix #2518, #2529, and various other fixes for shortcut key confusion
* Bug fix #2483, 2520, 2524: change in bdb attributes and methods
* Bug fix #2512: python 2.6 support
* Bug fix #2485: cannot create new family tree
* Bug fix #2507: unhandled exception when pasting invalid string
* Bug fix #2503: change to use of md5 module
* Bug fix to .desktop file

2008-10-19
Version 3.0.3 -- the "I have this terrible feeling of déjà vu" release.
* Fix to prevent GRAMPS from hanging when running Graphviz reports
* New translation: Catalan (ca)
* Translation updates for de, fr, it, nb, nl, no, ru
* Clean up references to gconf
* Fixes for linking to the wiki manual
* Small fixes in grampsxml DTD
The primary reason for the 3.0.3 release is to fix the Graphviz report hang issue introduced in 3.0.2.

2008-09-27
Version 3.0.2 -- the "You look like a milkman to me" release.
* Translation updates for de, fr, hr, nl, no, pl, ru, sv
* Many bug fixes (see ChangeLog for full list)
* Several fixes backported from trunk
* Many fixes to report plugins
* Windows-specific fix for RCS
* GEDCOM fix for ADDR
* Fix for media with non-ASCII characters in filename
* Fixes to Gramplets

2008-05-17
Version 3.0.1 -- the "Don't call me "Señor!" release!
* Translation updates for de, es, fi, fr, hr, lt, nb, nl, pl, sk, and sv!
* Bug fixes for the book report!
* Various improvements for the Relationship, Familylines and Hourglass graphs!
* Improvements to the narrative web report!
* Many miscellaneous bug fixes!
* See ChangeLog for full list of changes!

2008-03-24
Version 3.0.0 -- the "It was just getting interesting." release
* Rewrite of the GEDCOM parser
* Export views to a spreadsheet
* Formatted notes
* Multiple notes
* LDS temple definitions moved to supporting file
* New database format, using hidden directory, old grdb format deprecated
* New database manager, allowing create, deletion, renaming, repair and
  revison control

Version 2.2.10 -- the "Lemon Curry?" release

Version 2.2.9 -- the "Here's your ninepence" release

Version 2.2.8 -- the "You sons of a silly person" release

Version 2.2.7 -- the "Well, I didn't vote for you." release

Version 2.2.6 -- the "Summarize Proust Competition" release
* Fix report option saving

Version 2.2.5 -- the "Now go away or I shall taunt you a second time" release
* Peformance optimizations (Don Allingham, Alex Roitman, Richard Taylor)
* New date entry provides a new visual indicator (fade in/out of background
  color) instead of the old "LED" buttons. (Zsolt Foldvari)
* Keybindings added for list views (Don Allingham, Benny Malengier)
* New Birthay and Anniversaries report (Douglas Blank)
* Better error checking
* Better longitude/lattitude handling, mapping (Benny Malengier, Zolt Foldvari)
* Bug fixes (Don Allingham, Martin Hawlisch, Brian Matherly, Alex Roitman,
  Douglas Blank, Stefan Bjork, Richard Taylor)

Version 2.2.4 -- the "When you're chewing on life's gristle, Don't grumble, give a whistle" release
* Improved handling of readonly files
* Enhanced parsing of longitute and latitude and mapping
  (Benny Malengier/Zsolt Foldvari)
* Check and repair improvements
* Reference map rebuild tool
* New marker-based filters in the sidebar (Martin)
* Bug fixes

Version 2.2.3 -- the "My philosophy, like color television, is all there in black and white" release
* Per-database environment directories.
* Editor windows remember their size.
* Improved handling for invalid FTM GEDCOM.
* Reports use only primary events.
* Slovak manual is available (Lubo Vasko).
* Turkish translation added (Mehmet Ugur Kecik).
* Autobackup feature will save data on exit in XML format
* Many edit dialogs now save their last size
* Relationship View enhancements - scrolling and button handling
* Bug fixes

Version 2.2.2 -- the "We interrupt this program to annoy you and make things generally irritating" release
* Reordering for spouses and parents in the Relationships View.
* Performance improvements for the typeahead find in People View.
* Bug fixes.

Version 2.2.1 -- the "One, two, five!" release
* French manual is available (Jerome Rapinat).
* Bug fixes.

Version 2.2.0rc2 -- the "What is your quest?" release
* Bug fixes

Version 2.2.0rc1 -- the "Help, Help! I'm being repressed!" release
* Address has county, Location has street now.
* Improved icons (James Leigh).
* DB transactions are adjusted by the user.
* Drag and Drop improvements.
* Czech relationship calculator (Zdenek Hatas).
* Bug fixes.

Version 2.1.95 -- the "Listen! I can't give it to you now. It says, 'in the event of death'. Uh. Oh! Ah. Ah. Eh." release
* Removal of StartupUp Dialog
* New Media Manager tool.
* Support for attributes in events and event references;
  Support for AGE and AGENCY tags in GEDCOM.
* New Media Manager tool: advanced batch operations on media objects/files
* Verification tool displays disconnected people
* Lots of bug fixes

Version 2.1.91 -- the "Strange women lying in ponds distributing swords
is no basis for a system of government" release
* Transaction-protected metadata (Alex)
* DnD fixes (Don)
* Sidebar and custom filters for all object types (Alex)
* Performance optimization (Zsolt)
* New functionality for Fan Chart (Manfred Paulus)
* Filter fixes for person-based rules (Alex)
* Windows compatibility improvements (Brian)
* Custom name display improvements(Zsolt,Alex)
* Report fixes (Brian,Alex)
* Filters support for all object types (Don)
* Bug fixes

Version 2.1.90
* Windows installer (Steve Hall)
* Google maps lookup for places (Don)
* Custom name display formats (Zsolt Foldvari)
* Report fixes (Brian)
* Sidebar filters (Don)
* Support for associations and ASSO gedcom tag (Don)
* Bug fixes

Version 2.1.5
* Table of Contents generation added to several reports and formats (Brian)
* Filter Editor enhanced and working for Person filters (Don)
* Report modules restructured (Alex)
* Bug fixes

Version 2.1.4
* Enhanced Verify tool (Alex)
* Start of index generation for some reports in Open Document files (Brian)
* Report enhancements (Brian)
* Merge added in (Don)
* Shading option to highlight data in Relationship View (Don)
* Bug fixes.

Version 2.1.3
* Add user defined custom types to appropriate menus
* Select Place dialog replaces text entry of places
* Icon improvements
* Improved navigation in Pedigree View
* Fully functional side bar filter
* Bookmarks for all object types saved and loaded (XML)
* Marker colors are adjustable
* Bug fixes

Version 2.1.0 -- the "What are you going to do, bleed on me?" release
* Initial unstable release of 2.1.0.
* Far too many changes to specify. See http://gramps-project.org/whats_new/
