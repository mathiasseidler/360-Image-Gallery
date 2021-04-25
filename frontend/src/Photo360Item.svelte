<svelte:head>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/photo-sphere-viewer@4/dist/photo-sphere-viewer.min.css"
  />
</svelte:head>

<script>
  import { Viewer } from "photo-sphere-viewer";
  import { onMount } from "svelte";

  export let file_name;

  let container;

  onMount(() => {
    new Viewer({
      container: container.querySelector("#viewer"),
      panorama: file_name,
    });
  });
</script>
<div bind:this={container}>
  <div id="viewer" class="viewer" style="width:30vw;height:40vh;"/>
</div>

<!-- <style>
  .viewer {
    width: 20vw;
    height: 60vh;
  }
</style> -->





