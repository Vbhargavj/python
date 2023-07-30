#include <lame/lame.h>

int main()
{
    // Input and output file paths
    const char *inputFile = "input.mp3";
    const char *outputFile = "output.mp3";

    // Open the input file
    FILE *inputFilePtr = fopen(inputFile, "rb");
    if (!inputFilePtr)
    {
        printf("Failed to open input file: %s\n", inputFile);
        return 1;
    }

    // Open the output file
    FILE *outputFilePtr = fopen(outputFile, "wb");
    if (!outputFilePtr)
    {
        printf("Failed to open output file: %s\n", outputFile);
        fclose(inputFilePtr);
        return 1;
    }

    // Initialize the MP3 encoder
    lame_t lame = lame_init();
    lame_set_in_samplerate(lame, 44100);  // Set the input sample rate (adjust as needed)
    lame_set_out_samplerate(lame, 44100); // Set the output sample rate (adjust as needed)
    lame_set_num_channels(lame, 2);       // Set the number of channels (adjust as needed)
    lame_set_mode(lame, STEREO);          // Set the output mode to stereo

    // Set up the bass boost equalizer
    lame_set_bassboost(lame, 12); // Adjust the bass boost level (in dB) as needed

    // Initialize the MP3 encoder
    if (lame_init_params(lame) < 0)
    {
        printf("Failed to initialize the MP3 encoder\n");
        fclose(inputFilePtr);
        fclose(outputFilePtr);
        return 1;
    }

    // Read and process audio data in chunks
    const int bufferSize = 8192;
    short int pcmBuffer[bufferSize];
    unsigned char mp3Buffer[bufferSize];
    int bytesRead, bytesEncoded;

    do
    {
        // Read audio data from the input file
        bytesRead = fread(pcmBuffer, sizeof(short int), bufferSize, inputFilePtr);

        // Encode the audio data to MP3
        bytesEncoded = lame_encode_buffer(lame, pcmBuffer, NULL, bytesRead, mp3Buffer, bufferSize);

        // Write the encoded MP3 data to the output file
        fwrite(mp3Buffer, 1, bytesEncoded, outputFilePtr);
    } while (bytesRead != 0);

    // Flush the remaining MP3 data
    bytesEncoded = lame_encode_flush(lame, mp3Buffer, bufferSize);
    fwrite(mp3Buffer, 1, bytesEncoded, outputFilePtr);

    // Clean up and close the files
    lame_close(lame);
    fclose(inputFilePtr);
    fclose(outputFilePtr);

    printf("Bass boost applied successfully\n");

    return 0;
}
