import Konva from "konva";
import loadObjects from "./my_api_call.js"

// Declare globally so they can be accessed by other functions
let stage;
let layer;

window.addEventListener('DOMContentLoaded', () => {
  // Initialize Konva stage and layer when the page loads
  stage = new Konva.Stage({
    container: 'app', // id of the div
    width: window.innerWidth,
    height: window.innerHeight
  });

  layer = new Konva.Layer();
  stage.add(layer);

  console.log('Konva stage and layer initialized');
});

// Example: Button adds a circle when clicked
document.getElementById('myButton').addEventListener('click', () => {
  if (!stage || !layer) {
    console.error('Stage or layer not initialized yet!');
    return;
  }

  const group = new Konva.Group({
      draggable: true
  })
  layer.add(group);

  const complexText = new Konva.Text({
    x: 20,
    y: 60,
    text: "COMPLEX TEXT\n\nAll the world's a stage, and all the men and women merely players. They have their exits and their entrances.",
    fontSize: 18,
    fontFamily: 'Calibri',
    fill: '#555',
    width: 300,
    padding: 20,
    align: 'center'
  });

  const rect = new Konva.Rect({
    x: 20,
    y: 60,
    stroke: '#555',
    strokeWidth: 5,
    fill: '#ddd',
    width: 300,
    height: complexText.height(),
    shadowColor: 'black',
    shadowBlur: 10,
    shadowOffsetX: 10,
    shadowOffsetY: 10,
    shadowOpacity: 0.2,
    cornerRadius: 10
  });

  group.add(rect);
  group.add(complexText);

  layer.draw();
});

document.getElementById('myAPIButton').addEventListener('click', () => {
  if (!stage || !layer) {
    console.error('Stage or layer not initialized yet!');
    return;
  }
  const newObj = loadObjects();
  console.log("Added:", newObj);
});
