# AutoMarkdownContents

Automatically generate a Contents section in your readme
# Contents
<!-- AutoContentStart -->
- [Example use](#example-use)
- [How to use](#how-to-use)
    * [Params](#params)
        - [Auto](#auto)
        - [Skip First](#skip-first)

<!-- AutoContentEnd -->
> Proudly auto-generated!
# Example use
```yaml
steps:
  - uses: actions/checkout@v3
  - uses: thatrandomperson5/AutoMarkdownContents@v0.0.3
    with:
      file: README.md
      auto: true
```
# How to use
It will automatically generate an `contents.md` with a nested list as the table of contents. Each list item is properly linked up to the right url. Example below for [`test.md`](https://github.com/thatrandomperson5/AutoMarkdownContents/blob/main/test.md)
```md
- [Et orantem](#et-orantem)
    * [Variarum cinnamaque huic accedere laudat Mygdoniusque margine](#variarum-cinnamaque-huic-accedere-laudat-mygdoniusque-margine)
    * [Tenent Phrygum animam ignorat humo versato](#tenent-phrygum-animam-ignorat-humo-versato)
    * [Speciem saxa mutatus portas Gangetica titulum cuncti](#speciem-saxa-mutatus-portas-gangetica-titulum-cuncti)
- [Bello ero ferit](#bello-ero-ferit)
    * [Virgineis neque collecti](#virgineis-neque-collecti)
    * [In igneus tenuantur super](#in-igneus-tenuantur-super)
    * [Nocte et confiteor equos](#nocte-et-confiteor-equos)
    * [Bello fortis convellere liventia](#bello-fortis-convellere-liventia)

```
## Params
Here is some info about the params you can pass using the `with:` yaml syntax
|Name|cli param|description|
|-|-|-|
|Auto|`-a`|Automatically fill in the contents section|
|Exclude|`-e`|Exclude this header from the markdown, may mess up indentation|
|Skip first|`--skip-first`|Toggle off the skipping of the fist header|
### Auto
The auto paramater can be passed with `auto: true`. This parameter is equivalent to `-a` when using the cli tool. It automatically puts the contents in-between these two comments:
```html
<!-- AutoContentStart -->
<!-- AutoContentEnd -->
```
Everything in the middle will be replaced by the contents.
### Skip First
Can be passed with `skip-first: true`. Toggles off the defualt skip first param that is used to skip the title.
