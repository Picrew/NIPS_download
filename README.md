# NIPS  download 

## Explain 

​	Download NIPS all PDF files by ***Python web crawlers*** and  ***IDM Batch downloads***.

* [NeurIPS Proceedings](https://proceedings.neurips.cc//)

## Requirements

	* Requests
	* Bs4



## Python web crawlers

### Only download ###

```bash
python download.py
```

​	Then find useful Abstract-links.txt 

```bash
mv paper/Advances_in_Neural_Information_Processing_Systems_36__(NeurIPS_2023)/links.txt ../..
```

### Converted PDF links ###

```bash
python Abstract_Paper.py
```

Get Paper_links.txt



## IDM Batch downloads

### File import by Paper_links.txt

![File import by Paper_links](./images/File_import_by_paper_links.jpg)

### Batch downloads

![Batch downloads](./images/Batch_download.jpg)

## Key words
```bash
python find_key_words.py
```
