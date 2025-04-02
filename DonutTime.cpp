#include <iostream>
#include <cmath>
#include <cstring>
#include <unistd.h> // for usleep

// Terminal size (adjust if needed)
const int width = 80;
const int height = 24;

// Buffers for characters and depth
char output[width * height];
float zBuffer[width * height];

// ASCII brightness levels
const char shades[] = ".,-~:;=!*#$@";

int main() {
    float A = 0, B = 0; // Rotation angles

    while (true) {
        // Reset output and z-buffer each frame
        std::memset(output, ' ', width * height);
        std::memset(zBuffer, 0, sizeof(zBuffer));

        for (float theta = 0; theta < 2 * M_PI; theta += 0.07f) {
            for (float phi = 0; phi < 2 * M_PI; phi += 0.02f) {
                // Torus radius settings
                float R1 = 1;   // Radius of circle
                float R2 = 2;   // Distance from center of hole to center of tube
                float K2 = 5;   // Distance from viewer
                float K1 = width * K2 * 3 / (8 * (R1 + R2));

                // 3D Coordinates
                float sinA = std::sin(A), cosA = std::cos(A);
                float sinB = std::sin(B), cosB = std::cos(B);
                float sinTheta = std::sin(theta), cosTheta = std::cos(theta);
                float sinPhi = std::sin(phi), cosPhi = std::cos(phi);

                // Surface point coordinates after rotation
                float circleX = R2 + R1 * cosTheta;
                float circleY = R1 * sinTheta;

                // Final 3D position
                float x = circleX * (cosB * cosPhi + sinA * sinB * sinPhi) - circleY * cosA * sinB;
                float y = circleX * (sinB * cosPhi - sinA * cosB * sinPhi) + circleY * cosA * cosB;
                float z = K2 + cosA * circleX * sinPhi + circleY * sinA;
                float ooz = 1 / z;

                // Project to screen
                int xp = (int)(width / 2 + K1 * ooz * x);
                int yp = (int)(height / 2 - K1 * ooz * y);

                // Compute luminance (light effect)
                float L = cosPhi * cosTheta * sinB - cosA * cosTheta * sinPhi -
                          sinA * sinTheta + cosB * (cosA * sinTheta - cosTheta * sinA * sinPhi);

                // Only draw if inside screen bounds
                int idx = xp + yp * width;
                if (idx >= 0 && idx < width * height) {
                    if (ooz > zBuffer[idx]) {
                        zBuffer[idx] = ooz;
                        int luminanceIndex = (int)(L * 8);
                        if (luminanceIndex > 0)
                            output[idx] = shades[luminanceIndex];
                        else
                            output[idx] = '.';
                    }
                }
            }
        }

        // Output the frame
        std::cout << "\x1b[H"; // ANSI escape to reset cursor to top-left
        for (int k = 0; k < width * height; k++) {
            std::cout << (k % width ? output[k] : '\n');
        }

        A += 0.04f; // Rotate
        B += 0.02f;
        usleep(30000); // Delay to slow down the frame rate
    }

    return 0;
}
