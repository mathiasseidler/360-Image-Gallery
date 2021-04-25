<script>
  import Project360Collection from "./Project360Collection.svelte";
  import ProjectUploadForm from "./ProjectUploadForm.svelte";
  
  let files;
  const file_types = "image/png, image/jpeg";
  async function upload() {
    if (files.length > 0) {
      const formData = new FormData();
      for (let i = 0; i < files.length; i++) {
        formData.append("file", files[i]);
      }
      const response = await fetch("/upload", {
        method: "POST",
        body: formData,
      });
      // statusCode = response.status;
    }
  }
</script>

<ProjectUploadForm/>
<!-- <label for="360photo">Upload a 360 picture:</label>
<form class="content">
<label for="ProjectName">Nome</label><input id="ProjectName" type="text" bind:value={Project.name} />
<input accept={file_types} bind:files id="360photo" name="360photo" type="file" multiple/>
{#if files && files[0]}
  <button on:click={upload}>Submit</button>
{:else}
  <button on:click={upload} disabled>Submit</button>
{/if} -->

<Project360Collection file_name="images/IMG_20210310_163325_842.jpg"/>
<Project360Collection file_name="images/timothy-oldfield-luufnHoChRU-unsplash.jpg" />