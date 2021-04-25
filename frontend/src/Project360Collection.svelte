<script>
    import Photo360Item from "./Photo360Item.svelte";
    export let file_name;
    export let project = "Default";
    export let date = "2020-Mar-01";
    export let picture_description = "blala";
    //   export let width = 10;
    //   export let height = 10;
</script>
<style>
    h1 {
        color: rgb(0, 0, 0);
        font-family: "Helvetica Neue", sans-serif;
        font-size: 22pt;
        font-weight: 500;
    }
    h2 {
        color: rgb(0, 0, 0);
        font-family: "Helvetica Neue", sans-serif;
        font-size: 20px;
        font-weight: 300;
        margin: 0 0 0px;
    }
</style>


<h2>{project}</h2>
<h2> {date}</h2>
{picture_description}
<Photo360Item {file_name} />
