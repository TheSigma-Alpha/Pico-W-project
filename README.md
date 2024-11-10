# Pico-W-project
  <h1>Raspberry Pi Pico W Project Setup</h1>

  <h2>Required Materials</h2>
  <ul>
      <li>Raspberry Pi Pico W</li>
      <li>Buzzer</li>
      <li>Red, green, and blue LEDs</li>
      <li>Potentiometer</li>
      <li>Button</li>
      <li>Wires</li>
      <li>2 Breadboards</li>
      <li>Laptop</li>
      <li>Connection cable from Pico W to laptop</li>
  </ul>

  <h2>Instructions</h2>

  <h3>Step 1: Setting Up LEDs</h3>
  <p>Get three different colored LEDs: green, red, and blue. Place them in a line in the following positions:</p>
  <ul>
      <li>Green LED in pin <strong>1</strong></li>
      <li>Red LED in pin <strong>4</strong></li>
      <li>Blue LED in pin <strong>5</strong></li>
  </ul>
  <p>Position the LEDs in breadboard locations <strong>23, 25, and 27</strong>. Connect each LED’s negative end to the negative chain on the left.</p>

  <h3>Step 2: Setting Up the Buzzer</h3>
  <p>Place the buzzer in position <strong>30</strong>. Connect it to ground via the negative chain and to <strong>pin 9</strong>.</p>

  <h3>Step 3: Setting Up the Potentiometer</h3>
  <p>On another breadboard, place the potentiometer with the following pin connections:</p>
  <ul>
      <li>Pin <strong>14</strong> connected to ground</li>
      <li>Pin <strong>16</strong> (SIG) connected to <strong>pin 10</strong></li>
      <li>Pin <strong>18</strong> (VCC) connected to pin <strong>1</strong></li>
  </ul>
  <p>Connect the ground to the negative line on the opposite side.</p>

  <h3>Step 4: Setting Up the Button</h3>
  <p>Place the button and connect it as follows:</p>
  <ul>
      <li>Button pins connected to <strong>pin 6</strong> and <strong>pin 8</strong></li>
      <li>Ground pin of the button connected to the negative line on the second breadboard</li>
      <li>Other side of the button connected to <strong>pin 19</strong></li>
  </ul>

  <h3>Step 5: Coding in Visual Studio</h3>
  <p>Insert the code into Visual Studio Code, and set up the MicroPico extension to enable communication between your computer and the device. Make sure you have the correct cable to connect the Pico W to your laptop.</p>
