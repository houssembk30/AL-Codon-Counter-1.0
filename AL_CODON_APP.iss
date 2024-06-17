[Setup]
; Nom de l'application
AppName=AL Codon Counter
; Version de l'application
AppVersion=1.0
; R�pertoire d'installation par d�faut
DefaultDirName={commonpf}\AL Codon Counter
; Dossier de l'application dans le menu d�marrer
DefaultGroupName=AL Codon Counter
; Fichier de sortie
OutputBaseFilename=AL_Codon_Counter_Installer
; Ic�ne de l'installation
SetupIconFile=F:\AL CODON APP FINAL VERSION\JPG_PNG IMAGES\logo_ICON.ico
; Compresser l'installeur
Compression=lzma
; R�duire la taille du fichier d'installation
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"
Name: "bulgarian"; MessagesFile: "compiler:Languages\Bulgarian.isl"
Name: "catalan"; MessagesFile: "compiler:Languages\Catalan.isl"
Name: "corsican"; MessagesFile: "compiler:Languages\Corsican.isl"
Name: "czech"; MessagesFile: "compiler:Languages\Czech.isl"
Name: "danish"; MessagesFile: "compiler:Languages\Danish.isl"
Name: "dutch"; MessagesFile: "compiler:Languages\Dutch.isl"
Name: "finnish"; MessagesFile: "compiler:Languages\Finnish.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"
Name: "icelandic"; MessagesFile: "compiler:Languages\Icelandic.isl"
Name: "italian"; MessagesFile: "compiler:Languages\Italian.isl"
Name: "japanese"; MessagesFile: "compiler:Languages\Japanese.isl"
Name: "norwegian"; MessagesFile: "compiler:Languages\Norwegian.isl"
Name: "polish"; MessagesFile: "compiler:Languages\Polish.isl"
Name: "portuguese"; MessagesFile: "compiler:Languages\Portuguese.isl"
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "slovak"; MessagesFile: "compiler:Languages\Slovak.isl"
Name: "slovenian"; MessagesFile: "compiler:Languages\Slovenian.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"
Name: "turkish"; MessagesFile: "compiler:Languages\Turkish.isl"
Name: "ukrainian"; MessagesFile: "compiler:Languages\Ukrainian.isl"

[Files]
; Inclure tous les fichiers de l'application
Source: "F:\AL CODON APP FINAL VERSION\dist\AL CODON Version 1.0 Folder\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; Cr�er un raccourci sur le bureau
Name: "{commondesktop}\AL Codon Counter"; Filename: "{app}\AL CODON Version 1.0.exe"; IconFilename: "{app}\JPG_PNG IMAGES\logo_ICON.ico"; WorkingDir: "{app}"
; Cr�er un raccourci dans le menu d�marrer
Name: "{group}\AL Codon Counter"; Filename: "{app}\AL CODON Version 1.0.exe"; IconFilename: "{app}\JPG_PNG IMAGES\logo_ICON.ico"; WorkingDir: "{app}"
; Ajouter une option de d�sinstallation dans le menu d�marrer
Name: "{group}\Uninstall AL Codon Counter"; Filename: "{uninstallexe}"

[Run]
; Ex�cuter l'application � la fin de l'installation
Filename: "{app}\AL CODON Version 1.0.exe"; Description: "{cm:LaunchProgram,AL Codon Counter}"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
; Supprimer le r�pertoire d'installation entier
Type: filesandordirs; Name: "{app}"

[InstallDelete]
; Supprimer les fichiers restants et les raccourcis
Type: files; Name: "{commondesktop}\AL Codon Counter.lnk"
Type: files; Name: "{group}\AL Codon Counter.lnk"
