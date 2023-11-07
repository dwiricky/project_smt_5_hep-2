% 1. Tentukan path ke folder yang berisi gambar
folderPath = 'D:\Kuliah\Semester 5\Project\Dataset\Hep-21\Hep-2\Nucleolar';

% 2. Baca semua berkas gambar dalam folder
imageFiles = dir(fullfile(folderPath, '*.png'));  % Ganti dengan ekstensi yang sesuai

% 3. Loop melalui semua berkas gambar
for i = 1:numel(imageFiles)
    % 4. Baca gambar
    imagePath = fullfile(folderPath, imageFiles(i).name);
    img = imread(imagePath);

    % 5. Naikkan kecerahan gambar (1,5x)
    brightened_img = 1.5 * img;

    % 6. Simpan gambar yang sudah ditingkatkan dengan nama yang sama (menimpa gambar asli)
    imwrite(brightened_img, imagePath);
end
