This folder contains the annotated documents for stage 1 of the project.

- Number of annotated documents: 330
- Entity: Any location that is a city, region, country, or continent.
- Annotation Tags: <loc> ... </loc>
- Example annotated entity: <loc>Silicon Valley</loc> is located in <loc>western <loc>United States</loc></loc>. 
    * Note that we also take into account cascaded locations. In the above example "western United States" is a different entity from "United States" so both are annotated.

Although, the folder contains 616 documents, we only annotated 330 of them. Documents 1-110, 200-310, and 400-510 are annotated. Most documents have at least 1 mention of the entity. A few of the documents do not have a single mention of the entity. We explicitly flag those no entity documents in their filenames. For instance file `459 - none.txt` has no entity mentioned in it.

Furthermore some of the documents we downloaded were very similar or exactly the same to each other. We also flags these documents. For instance `464 - similar.txt` and `465 - similar.txt` were exactly the same document so we only consider a single instance of that document.