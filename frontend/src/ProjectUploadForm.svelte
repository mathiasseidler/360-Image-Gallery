<script>
  let files;
  let form_data;
  let preview_images = [];
  let name;
  let date;
  let description;
  const file_types = "image/png, image/jpeg";

  async function upload() {
    const formData = new FormData(form_data);
    formData.append("ProjectName", name);
    formData.append("ProjectDescription", description);
    formData.append("Date", date)
    await fetch("/upload", {
        method: "POST",
        body: formData,
      });
    form_data.reset();
    files = [];
       
  }

  async function onFileSelected(event){
    preview_images = [];
    for ( let i = 0; i < event.target.files.length; i++){
      let image = event.target.files[i];
      let reader = new FileReader();
      reader.onload = (e) => {
        preview_images = [...preview_images, e.target.result];
      };
      reader.readAsDataURL(image);
    }
  }
</script>

<h1>Project Upload</h1>
<form on:submit|preventDefault={upload} bind:this={form_data} class="content">
  <label for="ProjectName" >Project name</label>
  <input id="ProjectName" type="text" bind:value={name} placeholder="Name and location of the project"/>
  <label for="ProjectDate">Date</label>
  <input id="ProjectDate" type="date" bind:value={date}/>
  <label for="ProjectDescrip">Description</label>
  <input id="ProjectDescrip" type="text" bind:value={description} placeholder="Living room 20sqm, 2 bathroom, ..."/>
  <label for="360photos">Select files</label>
  <input
    accept={file_types}
    bind:files
    on:change={(e) => onFileSelected(e)}
    id="360photos"
    name="360photos"
    type="file"
    multiple
  />
  {#if files && files[0]}
    <input type="submit" value="Submit" id="btnsubmit" />
  {:else}
    <input type="submit" value="Submit" id="btnsubmit" disabled/>
  {/if}
</form>

{#if files && files[0]}
  {#each preview_images as file}
    <img src={file} alt="" width="100" height="80"/>
  {/each}
{/if}


<style>
  .content {
    display: grid;
    grid-template-columns: 10% 30%;
    grid-column-gap: 10px;
  }
  img {
    margin: 0px 5px;
  }
</style>
