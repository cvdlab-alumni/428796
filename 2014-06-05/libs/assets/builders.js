



var lampShadowRadius;
var baseHeight;
var jointRadius;
var squareSide;
var armHeight;





function makeDesk(width,depth,height,segmentWidth,segmentDepth,segmentHeight,colore) {
  var deskGeometry = new THREE.BoxGeometry(width,depth,height,segmentWidth,segmentDepth,segmentHeight);
  var deskMaterial = new THREE.MeshPhongMaterial( {color: colore, transparent: true, opacity: 0.8, shininess: 60} );
  var desk = new THREE.Mesh(deskGeometry, deskMaterial);

  desk.castShadow = true;
  desk.receiveShadow = true;
  return desk;
}

function makeLeg(radiusTop, radiusBottom, height, radiusSegments, heightSegments, colore) {
  var legGeometry = new THREE.CylinderGeometry(radiusTop, radiusBottom, height, radiusSegments, heightSegments);
  var legMaterial = new THREE.MeshPhongMaterial( {color: colore} );
  var leg = new THREE.Mesh( legGeometry, legMaterial );

  leg.castShadow = true;
  leg.receiveShadow = true;
  return leg;
}

function tableBuilder(deskWidth,deskDepth,deskHeight,deskSegmentWidth,deskSegmentDepth,deskSegmentHeight,deskColore,   legRadiusTop, legRadiusBottom, legHeight,legRradiusSegments, legHeightSegments, legColore) {
  var desk = makeDesk(deskWidth,deskDepth,deskHeight,deskSegmentWidth,deskSegmentDepth,deskSegmentHeight,deskColore);
  var leg1 = makeLeg(legRadiusTop, legRadiusBottom, legHeight,legRradiusSegments, legHeightSegments, legColore);
  var leg2 = makeLeg(legRadiusTop, legRadiusBottom, legHeight,legRradiusSegments, legHeightSegments, legColore);
  var leg3 = makeLeg(legRadiusTop, legRadiusBottom, legHeight,legRradiusSegments, legHeightSegments, legColore);
  var leg4 = makeLeg(legRadiusTop, legRadiusBottom, legHeight,legRradiusSegments, legHeightSegments, legColore);

  leg1.rotation.x = -Math.PI/2;
  leg2.rotation.x = -Math.PI/2;
  leg3.rotation.x = -Math.PI/2;
  leg4.rotation.x = -Math.PI/2;

  desk.position.set((deskWidth)/2, (deskDepth)/2, legHeight);
  leg1.position.set(legRadiusTop, legRadiusTop, legHeight/2);
  leg2.position.set(deskWidth-legRadiusTop, legRadiusTop, legHeight/2);
  leg3.position.set(deskWidth-legRadiusTop, deskDepth-legRadiusTop, legHeight/2);
  leg4.position.set(legRadiusTop, deskDepth-legRadiusTop, legHeight/2);

  var tavolo = new THREE.Object3D();

  tavolo.add(desk);
  tavolo.add(leg1);
  tavolo.add(leg2);
  tavolo.add(leg3);
  tavolo.add(leg4);

  return tavolo;
}
function baseBuilder(radiusTop, radiusBottom, height, radiusSegments, heightSegments, colore, tableHeight, tableWidth, tableDepth) {

  var baseGeometry = new THREE.CylinderGeometry(radiusTop, radiusBottom, height, radiusSegments, heightSegments);
  var baseMaterial = new THREE.MeshPhongMaterial( {color: colore, shininess: 80, specular: colore,metal:true} );
  var base = new THREE.Mesh( baseGeometry,baseMaterial );
  baseHeight = height;
  base.position.set(tableWidth/2, tableDepth/2, tableHeight);
  base.rotation.x = -0.5 *Math.PI;
  return base;
}

function jointBuilder(radius, widthSegments, heightSegments, colore) {
  var jointGeometry = new THREE.SphereGeometry(radius, widthSegments, heightSegments);
  var jointMaterial = new THREE.MeshPhongMaterial( {color: colore, shininess: 80, specular: colore,metal:true} );
  var joint = new THREE.Mesh( jointGeometry, jointMaterial );
  jointRadius = radius;
  joint.position.set(0,-baseHeight/2 - radius,0);
  return joint;
}
function squaredBaseBuilder(side1,side2, colore) {
  var geometry = new THREE.PlaneGeometry( side1, side2 );
  var material = new THREE.MeshPhongMaterial( {color: colore, side: THREE.DoubleSide, shininess: 80, specular: colore,metal:true} );
  var plane = new THREE.Mesh( geometry, material );
  squareSide = side1;
  plane.rotation.x = 0.5*Math.PI;
  plane.position.set(0,-jointRadius,0)
  return plane;
}

  function armBuilder(radiusTop, radiusBottom, height, radiusSegments, heightSegments, colore) {
    var armGeometry = new THREE.CylinderGeometry(radiusTop, radiusBottom, height, radiusSegments, heightSegments);
    var armMaterial = new THREE.MeshPhongMaterial({color: colore, shininess: 80, specular: colore, metal:true});
  
    var arm1 = new THREE.Mesh( armGeometry, armMaterial );
    var arm2 = new THREE.Mesh( armGeometry, armMaterial );
    var arm3 = new THREE.Mesh( armGeometry, armMaterial );
    var arm4 = new THREE.Mesh( armGeometry, armMaterial );

    armHeight = height;

    arm1.position.set(squareSide/2-radiusTop,height/2,squareSide/2-radiusTop);
    arm2.position.set(-squareSide/2+ radiusTop ,height/2, -squareSide/2 +radiusTop);
    arm3.position.set(-squareSide/2+ radiusTop ,height/2, squareSide/2 -radiusTop);
    arm4.position.set(squareSide/2- radiusTop ,height/2, -squareSide/2 +radiusTop);
    //sposta braccia agli angoli del quadrato poi aggiungu tutto a obj3d, sposta obj3d in alto e continua su tavolo.html

    var arms = new THREE.Object3D();
    arms.add(arm1);
    arms.add(arm2);
    arms.add(arm3);
    arms.add(arm4);
    arms.rotation.x = 0.5 * Math.PI;
    return arms;

  }


function squaredMiddleBaseBuilder(side1,side2, colore) {
  var geometry = new THREE.PlaneGeometry( side1, side2 );
  var material = new THREE.MeshPhongMaterial( {color: colore,side: THREE.DoubleSide, shininess: 80, specular: colore, metal:true} );
  var plane = new THREE.Mesh( geometry, material );
  squareSide = side1;
  plane.rotation.x = 0.5*Math.PI;
  plane.position.set(0,armHeight,0);
  return plane;
}

function upJointBuilder(radius, widthSegments, heightSegments, colore) {
  var jointGeometry = new THREE.SphereGeometry(radius, widthSegments, heightSegments);
  var jointMaterial = new THREE.MeshPhongMaterial( {color: colore, shininess: 80, specular: colore, metal:true} );
  var joint = new THREE.Mesh( jointGeometry, jointMaterial );
  jointRadius = radius;
  joint.position.set(0,0,-radius);
  return joint;

}
function lampShadowBuilder(radius, widthSegments, heightSegments, phiStart, phiLength,colore) {
  var lsGeometry = new THREE.SphereGeometry(radius, widthSegments, heightSegments, phiStart, phiLength);
  var lsMaterial = new THREE.MeshPhongMaterial( {color: colore,side: THREE.DoubleSide, shininess: 80, specular: colore, metal:true} );
  var ls = new THREE.Mesh( lsGeometry, lsMaterial );
  lampShadowRadius = radius;
  ls.position.set(0,0,-radius- jointRadius);
  return ls;
}

function bulbBuilder(radiusTop, radiusBottom, height, colore) {
  var bulbGeometry = new THREE.CylinderGeometry(radiusTop, radiusBottom, height);
  var bulbMaterial = new THREE.MeshLambertMaterial( {color: colore} );
  var bulb = new THREE.Mesh( bulbGeometry, bulbMaterial );

  bulb.rotation.x = 0.5*Math.PI;
  bulb.position.set(0,0,lampShadowRadius- height);
  return  bulb;
}
function lampBuilder(radius, widthSegments, heightSegments, colore) {
  var lampGeometry = new THREE.SphereGeometry(radius, widthSegments, heightSegments);
  var lampMaterial = new THREE.MeshPhongMaterial( {color: colore, transparent: true, opacity: 0.3, shininess: 80} );
  var lamp = new THREE.Mesh( lampGeometry, lampMaterial );
  lamp.position.set(0,0,radius/2);
  return lamp;
}


