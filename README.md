# 360-Image-Gallery
360 Image Gallery with Auth0 user management


360 Images are panoramic images capturing all directions around the camera. 
These pictures are typically viewed by projecting them on a sphere, which allows to explore the picture content in all directions with either a viewer where the field-of-view can be changed with either a VR headset or with mouse/keyboard.

Thes images are usefull for the real estated industry as all directions of the captures space can be seen, giving interested parties a good overview without a site visit. Architecture offices can use these pictures to accuratly present space to clients and remote colleagues who can not visit a site due to mobility restrictions.

This application is work-in-progress and its goal is to host 360 images of an Architecture company.
The app should allow creation of projects, editing projects and at one point access permission mgmt to allow the admin to expose galleries only to authorized users.

# Development stack:
Svelte.js providing a reactive frontend

Python FastAPI implementing a REST-ful API

Python for CRUD business logic using SQLalchemy's object relational mapper for data base transaction.

Data base: SQLite for local prototyping, Postgres for a later server-less deployment on Heroku

Authentication and user management: Auth0
