<script lang="ts">
  import { onDestroy, onMount } from "svelte";

  interface EntryData {
    x: number | boolean;
    y: number | boolean;
    p: boolean;
  }

  interface DataMap {
    [timestamp: number]: EntryData;
  }

  let data: DataMap = {};

  const startTime: number = Date.now();
  let interval;
  let oldMousePos = { x: 0, y: 0 };
  let newMousePos = { x: 0, y: 0 };

  function handleKeyDown() {
    const newTime = Date.now() - startTime;
    data[Math.round(newTime / 10)] = {
      x: false,
      y: false,
      p: false,
    };
    data = { ...data };
  }

  function handleMouseMove(e: MouseEvent) {
    newMousePos = { x: e.screenX, y: e.screenY };
  }

  function printArray() {
    navigator.clipboard.writeText(JSON.stringify(data));
  }

  function handleClick() {
    const newTime = Date.now() - startTime;
    data[Math.round(newTime / 10)] = {
      x: false,
      y: false,
      p: true,
    };
    data = { ...data };
  }

  function addMouseData() {
    const newTime = Date.now() - startTime;
    data[Math.round(newTime / 10)] = {
      x: newMousePos.x,
      y: newMousePos.y,
      p: false,
    };
    data = { ...data };
    oldMousePos = { ...newMousePos };
  }

  onMount(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("mousemove", handleMouseMove);
    window.addEventListener("click", handleClick);

    interval = setInterval(() => {
      if (oldMousePos.x !== newMousePos.x && oldMousePos.y !== newMousePos.y) {
        addMouseData();
      }
    }, 100);
  });

  onDestroy(() => {
    window.removeEventListener("keydown", handleKeyDown);
    window.removeEventListener("mousemove", handleMouseMove);
    window.removeEventListener("click", handleClick);
  });
</script>

<main>
  <div class="main">
    <button class="button" on:click={printArray}>PRINT</button>
    <div class="big">
      {#if Object.keys(data).length > 0}
        <!-- prints the latest time interval -->
        <div>{Object.keys(data)[Object.keys(data).length - 1]}</div>
      {/if}
    </div>
  </div>
</main>

<style>
  .main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .button {
    width: 200px;
    margin-bottom: 2em;
  }
  .big {
    height: 50vh;
    width: 75vw;
    background-color: grey;
    color: azure;
    overflow: auto;
  }
</style>
