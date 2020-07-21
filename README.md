# exposify

`exposify` is a tool to help the fight against disinformation.

# Permissions

Basically, what happens is when the URL that you're currently browsing matches with one that's in the list of URLs that are known bad actors, a warning is added to the page and the title of the page has "💀EXPOSED💀" added to it. In order to do that, the extension needs to know the current URL and be able to add (inject) HTML into the page. That means that this extension requires the `activeTab` persimission. From [Mozilla's docs](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/permissions#activeTab_permission):

<blockquote>
If an extension has the activeTab permission, then when the user interacts with the extension, the extension is granted extra privileges for the active tab only.

"User interaction" includes:
- the user clicks the extension's browser action or page action
- the user selects its context menu item
- the user activates a keyboard shortcut defined by the extension

The extra privileges are:
- The ability to inject JavaScript or CSS into the tab programmatically, using `browser.tabs.executeScript()` and `browser.tabs.insertCSS()`
- Access to the privileged parts of the tabs API for the current tab: `Tab.url`, `Tab.title`, and `Tab.faviconUrl`.

The intention of this permission is to enable extensions to fulfill a common use case, without having to give them very powerful permissions. Many extensions want to "do something to the current page when the user asks".
</blockquote>

None of this information is sent back to me, nor do I store it anywhere. Everything stays within your browser.
