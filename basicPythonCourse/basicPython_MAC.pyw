U
    ?��]]	 �                   @   s`   d dl Z d dlZd dlT d dlmZ d dlmZ d dlZG dd� d�Ze� Z	ee	�Z
e	��  dS )�    N)�*)�ttk)�redirect_stdoutc                   @   s|  e Zd Zdd� Zdd� Zdd� Zdd� Zd	d
� Zdd� Zdd� Z	dd� Z
dd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd � Zd!d"� Zd#d$� Zd%d&� Zd'd(� Zd)d*� Zd+d,� Zd-d.� Zd/d0� Zd1d2� Zd3d4� Zd5d6� Zd7d8� Zd9d:� Zd;d<� Z d=d>� Z!d?d@� Z"dAdB� Z#dCdD� Z$dEdF� Z%dGdH� Z&dIdJ� Z'dKdL� Z(dMdN� Z)dOdP� Z*dQdR� Z+dSdT� Z,dUdV� Z-dWdX� Z.dYdZ� Z/d[d\� Z0d]d^� Z1d_d`� Z2dadb� Z3dcdd� Z4dedf� Z5dgdh� Z6didj� Z7dkdl� Z8dmdn� Z9dodp� Z:dqdr� Z;dsdt� Z<dudv� Z=dwdx� Z>dydz� Z?d{d|� Z@d}d~� ZAdd�� ZBd�d�� ZCd�d�� ZDd�d�� ZEd�d�� ZFd�d�� ZGd�d�� ZHd�d�� ZId�d�� ZJd�d�� ZKd�d�� ZLd�d�� ZMd�d�� ZNd�d�� ZOd�d�� ZPd�S )��basicLearningc                 C   s�  d| _ d| _tj�tj�t��| _| jd | _| jd | _	| jd | _
d| _d| _| j s�t| jd d	�}|�� }|��  d
| j }|| }t| j	| j d�}|�|� |��  d}|| _| j�d| � d| _d| _t| j�d t| j� }| j�|� | j�dd� | jdk�r�d| _d| _d| _d| _| jddf| _| jddf| _| jddf| _| jddf| _| jddf| _ | jddf| _!| j!| _"| j!| _#| j#| _$| jddf| _%| jddf| _&| jddf| _'| jddf| _(| jddf| _)| jddf| _*| j*| _+| j*| _,| jddf| _-| j-| _.| j-| _/| jd df| _0d!| _1d"| _2d#| _3d$| _3d%| _4| j3| _5| j4| _6d&| _7d%| _8d'| _9d%| _:d(| _;d%| _<d(| _=d)| _>d*| _?�n�| jdk�rd| _d| _d| _d| _| jddf| _| jddf| _| jddf| _| jddf| _| jd+df| _ | jddf| _!| j!| _"| jd,df| _#| j!| _$| jddf| _%| jddf| _&| jd-df| _'| jddf| _(| jddf| _)| jddf| _*| j*| _+| j*| _,| jddf| _-| j-| _.| j-| _/| jd df| _0d!| _1d"| _2d#| _3d$| _3d%| _4| j3| _5d.| _6d&| _7d%| _8d'| _9d%| _:d(| _;d%| _<d(| _=d&| _>d'| _?nt@d/� tA| jd0 d1�| _BtA| jd2 d1�| _C| j�Dd3| jE� d4| _F| �G�  | �H�  | jIjJdtKd5� d6| _Ld S )7NT�macz/dataBasic/z	pageData/zimages/zc01s02h02.txti�  z/basicPython.py�r�
�wzv5.1zLeahurst Basic Python i4  i&  �xF�windowszMS SerifZCourierzTimes New RomanzComic Sans MS�+   Zbold�   �normalZitalic�
   �   �   �   �<   z#ccc8c8Zgroovez#00005az#002847ZwhiteZredZgreenZbluez#ff4545z#00ff00�   �   �   �black�ERROR: BAD OS MODE DEFINEDzlogo_transparent.png��filezlogo_small_transparent.pngz
<KeyPress>�   ��expand�fill�toc)MZ
distribute�osMode�os�path�dirname�realpath�__file__Zdir_path�rootPath�pageDataPath�	imagePath�	trickName�
offsetCode�open�read�close�write�root�titleZminXZminY�strZgeometryZ	resizableZ	fontName1Z	fontName2Z	fontName3Z	fontName4�titlePageFont�	titleFont�subtitleFont�subsectionFont�footFont�codeFont�
outputFont�addressFont�	notesFont�
buttonFont�lessonLabelFont�bigIdeaFont�explanationFont�projectFont�kuFont�tiFont�aFont�kuLabelFont�tiLabelFont�
aLabelFont�
noFileFont�buttonColour�buttonRelief�headerbgcolor�headerfgcolor�footerbgcolor�footerfgcolor�	kubgcolor�	kufgcolor�	tibgcolor�	tifgcolor�abgcolor�afgcolor�bigIdeaColor�lastLineColor�nextLineColor�print�
PhotoImage�logo�
logo_small�bind�keyPress_callback�	firstCall�loadProgramData�createWidgets�tocFrame�pack�BOTH�
whichFrame)�selfr/   r   �rawCodeZshiftedCode�versionZsizeWin� rf   �basicPython.py�__init__   s�    


zbasicLearning.__init__c                 C   s�  |j dks|j dkrz| jdkr(| ��  nN| jdkr<| ��  n:| jdkrP| ��  n&| jdkrd| ��  n| jdkrv| ��  �nn|j dks�|j d	kr�| jdkr�| ��  nN| jdkr�| ��  n:| jdkr�| �	�  n&| jdkr�| �
�  n| jdkr�| ��  n�|j d
k�s
|j dk�r�| jdk�r | ��  n�| jdk�r6| ��  n�| jdk�rL| ��  n�| jdk�rb| ��  n�| jdk�r�| j��  | jd dk�r�| ��  nV| jd dk�r�| ��  n<| jd dk�r�| ��  n"| jd dk�r�| ��  ntd� d S )Nr   �R�lesson�example�practice�project�noFile�p�P�n�Nr   ������e�h�m�ERROR)Zkeysymrb   �backTOC_lesson_callback�backTOC_example_callback�backTOC_practice_callback�backTOC_project_callback�backTOC_noFile_callback�prevPage_lesson_callback�prevPage_example_callback�prevPage_practice_callback�prevPage_project_callback�prevPage_noFile_callback�nextPage_lesson_callback�nextPage_example_callback�nextPage_practice_callback�nextPage_project_callbackr_   �forget�loadID�
loadLesson�loadExample�loadPractice�loadProjectrV   �rc   �eventrf   rf   rg   r[   �   sT    



























zbasicLearning.keyPress_callbackc                 C   s4   | � �  | ��  | ��  | ��  | ��  | ��  d S �N)�	createTOC�createLESSON�createEXAMPLE�createPRACTICE�createNOFILE�createPROJECT�rc   rf   rf   rg   r^   �   s    zbasicLearning.createWidgetsc                 C   s  t �t�| _t �| j�| _t �| j�| _t �| j�| _t| j�| _t| j�| _	t| j�| _
t �| j�| _| jdkr�t �| j�| _t �| j�| _t �| j�| _t �| j�| _nD| jdkr�t| j�| _t| j�| _t| j�| _t| j�| _ntd� | jjddd� | jjddd� | jjddd� | jjddd� | jjdddd	� | jjdddd	� | jjdddd	� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjd
d� | jjddddd� | jjdddd	� | jjdddd	� | jjdddd	� | jj| j| jd� | jj| j| j| jddd� | jj| j| j| jddd� | jj| j| j| jddd� | jjdtd� | jjd| jddd� | jjdddd	� | j	jdddd	� | j
jdddd	� | jdk�r|| jjd| j | j!| j"| j#d� | j	jd| j | j!| j"| j#d� | j
jd| j | j!| j"| j#dd� nr| jdk�r�| jjd| j | j!| j"| j#d� | j	jd| j | j!| j"| j#d� | j
jd| j | j!| j"| j#dd � ntd� | jj| j$d!� | j	j| j%d!� d S )"Nr   r   r   r   �Zweightr   �   �nwse��row�column�stick�ridge��relief�   �nsew�r�   r�   �rowspanr�   ��image�
background�leftr	   ��fontr�   �
foreground�justify�anchorTr   u   ¯\_(ツ)_/¯
FILE NOT FOUND�center)�textr�   r�   r�   �nswe�Return to T.O.C. (r)�r�   r�   r�   r�   r�   �Previous Page (p)�Next Page (n)�disabled)r�   r�   r�   r�   r�   �state�r�   r�   �highlightbackgroundr�   r�   )r�   r�   r�   r�   r�   r�   �Zcommand)&r   �Framer/   �noFileFrameZhead_noFileZbody_noFileZfoot_noFile�ButtonZbackTOC_noFileZprevPage_noFileZnextPage_noFile�LabelZlabel_noFiler    Zlogo_noFile�title_noFile�subtitle_noFile�subsection_noFilerV   �rowconfigure�columnconfigure�grid�configrY   rI   r3   rJ   r4   r5   r`   ra   rF   r6   rK   rL   rH   r|   r�   r�   rf   rf   rg   r�   �   sx    

""zbasicLearning.createNOFILEc                 C   s�   | j jdtd� d| _| j}|d dkr4| j| }nP|d dkrL| j| }n8|d dkrd| j| }n |d dkr|| j| }nt	d	� | j
j|d
 d� | jj|d d� | jj|d d� | j jdtd� d| _d S )NTr   Znofile�   ro   rt   ru   rv   rw   �chapter�r�   �section�
subsectionrn   )r�   r`   ra   rb   r�   �
lessonData�exampleData�practiceData�projectDatarV   r�   r�   r�   r�   �rc   �ID�datarf   rf   rg   �
loadNOFILE  s$    zbasicLearning.loadNOFILEc                 C   sZ   | j }| j�|�}| j��  |dkr>| jjdtd� | ��  n| j|d  | _ | �	�  d S �Nr   Tr   r   )
r�   �pageID�indexr�   r�   r_   r`   ra   �
prepareTOC�loadPage_callback�rc   r�   �indrf   rf   rg   r�   ,  s    

z&basicLearning.prevPage_noFile_callbackc                 C   s&   | j ��  | jjdtd� | ��  d S �NTr   )r�   r�   r_   r`   ra   r�   r�   rf   rf   rg   r|   7  s    
z%basicLearning.backTOC_noFile_callbackc                 C   s0  t �| j�| _t �| j�| _t �| j�| _t �| j�| _t �| j�| _| j	dkr�t �| j�| _
t �| j�| _t �| j�| _t �| j�| _nD| j	dkr�t| j�| _
t| j�| _t| j�| _t| j�| _ntd� t| j�| _t| j�| _t| j�| _t| j�| _t| j�| _t �| j�| _t �| j�| _| jjddd� | jjddd� | jjddd� | jjddd� | jjdddd	� | jjdddd	� | jjdddd	� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjd
d� | j
jddddd� | jjdddd	� | jjdddd	� | jjdddd	� | j
j| j| jd� | jj| j| j| jddd� | jj| j | j| jddd� | jj| j!| j| jddd� | jjddddd� | jjdd� | jjdddd	� | jjdddd	� | jj"t#dd� | jj"t#dd� | jj| j$d� | jj| j$d� | jjddd� | jjddd� | jj| j%dddd� | jj| j&dddd� | jjdddd	� | jjdddd	� | jjdddd	� | j	dk�r�| jjd | j'| j(| j)| j*d!� | jjd"| j'| j(| j)| j*d!� | jjd#| j'| j(| j)| j*d!� np| j	dk�r�| jjd | j'| j(| j)| j*d$� | jjd"| j'| j(| j)| j*d$� | jjd#| j'| j(| j)| j*d$� ntd� | jj| j+d%� | jj| j,d%� | jj| j-d%� d S )&Nr   r   r   r   r�   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r	   r�   �solidT)r   r   �r�   zBig Idearq   )r�   �labelanchorZExplanationi�  r�   )r�   �
wraplengthr�   r�   )r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   ).r   r�   r/   �lessonFrameZhead_lessonZbody_lessonZfoot_lessonr�   �image_lessonr    Zlogo_lesson�title_lesson�subtitle_lesson�subsection_lessonrV   �
LabelFrameZbigIdea_lessonZexplanation_lessonr�   ZbackTOC_lessonZprevPage_lessonZnextPage_lesson�bigIdea_text�explanation_textr�   r�   r�   r�   rY   rI   r3   rJ   r4   r5   r`   ra   r<   r=   r>   r6   rK   rL   rH   rx   r�   r}   r�   rf   rf   rg   r�   @  s�    

  zbasicLearning.createLESSONc                 C   sZ   | j }| j�|�}| j��  |dkr>| jjdtd� | ��  n| j|d  | _ | �	�  d S r�   )
r�   r�   r�   r�   r�   r_   r`   ra   r�   r�   r�   rf   rf   rg   r}   �  s    

z&basicLearning.prevPage_lesson_callbackc                 C   s<   | j }| j�|�}| j|d  }|| _ | j��  | ��  d S �Nr   )r�   r�   r�   r�   r�   r�   �rc   r�   r�   ZnextIDrf   rf   rg   r�   �  s    
z&basicLearning.nextPage_lesson_callbackc                 C   s&   | j ��  | jjdtd� | ��  d S r�   )r�   r�   r_   r`   ra   r�   r�   rf   rf   rg   rx   �  s    
z%basicLearning.backTOC_lesson_callbackc                 C   s�   | j }| j| d s| ��  n�| j| }| jj|d d� | jj|d d� | jj|d d� | jj|d d� | jj|d �	d	�| j
d
� | jj|d d� | jjdtd� d| _d S )N�
fileExistsr�   r�   r�   r�   �img)r�   �bigIdear   �r�   r�   �explanationTr   rj   )r�   r�   r�   r�   r�   r�   r�   r�   r�   �striprS   r�   r�   r`   ra   rb   r�   rf   rf   rg   r�   �  s    

zbasicLearning.loadLessonc                 C   s�  t �| j�| _t �| j�| _t �| j�| _t �| j�| _| jdkr|t �| j�| _	t �| j�| _
t �| j�| _t �| j�| _nD| jdkr�t| j�| _	t| j�| _
t| j�| _t| j�| _ntd� t j| jdd�| _t j| jdd�| _t j| jdd�| _t j| jdd�| _t j| jd	d�| _t| j�| _t| j�| _t j| jd
d�| _t j| jdd�| _t| j�| _t| j�| _t �| j�| _t| j�| _t| j�| _ t| j�| _!t| j�| _"| jj#ddd� | jj#ddd� | jj#ddd� | jj$ddd� | jj%dddd� | jj%dddd� | jj%dddd� | jj#ddd� | jj#ddd� | jj#ddd� | jj$ddd� | jj$ddd� | jj$ddd� | jj#ddd� | jj$ddd� | jj$ddd� | jj$ddd� | jj&dd� | j	j%ddddd� | j
j%dddd� | jj%dddd� | jj%dddd� | j	j&| j'| j(| j)d� | j
j&| j*| j(| j)ddd� | jj&| j+| j(| j)ddd� | jj&| j,| j(| j)ddd� | jj&dd� | jj%ddddd� | jj%ddddd� | jj%ddddd� | jj%ddddd� | jj%ddddd� | jj&dd� | jj&dd� | jj&dd� | jj&dd� | jj&dd� | jj&dd� | j�-�  | j�-�  | jj%ddd � | jj%dddd!� | j�-�  | j�-�  | j�-�  | j�-�  | j j%dddd� | j!j%dddd� | j"j%dddd� | jdk�rL| j j&d"| j.| j/| j0| j1d#� | j!j&d$| j.| j/| j0| j1d#� | j"j&d%| j.| j/| j0| j1d#� d&}nt| jdk�r�| j j&d"| j.| j/| j0| j1d'� | j!j&d$| j.| j/| j0| j1d'� | j"j&d%| j.| j/| j0| j1d'� d(}ntd� | j j&| j2d)� | jj&d*d+d,� | jj&| j3d-� | jj&|d+d,� | jj&| j4d-� | jj&d.d.d/� | jj&d0d1� | jj&d2d.d/� | jj&d0d1� | jj&| j5d-� | jj&| j5d-� | jj&d3dd4� | jj&|d5d0d6� | jj&| j6d-� | j"j&| j7d)� | j!j&| j8d)� d S )7Nr   r   r   zSOURCE CODEr�   zSCREEN OUTPUTzSYMBOL TABLEzProgram CounterZNOTESzSymbol NameZValuer   r�   r   r�   r�   r�   r�   r�   r�   r�   r�   �r�   r�   r�   r�   r	   r�   )Zpad�   Znwrq   )r�   �r�   r�   )r�   r�   �
columnspanr�   r�   r�   r�   �   r�   r   r�   r   �4   )�height�widthr�   r   )r�   r�   �word)�wrap�$   �readonly)r�   r�   �0   )r�   r�   r�   )9r   r�   r/   �exampleFrameZhead_exampleZbody_exampleZfoot_exampler    r�   Zlogo_example�title_example�subtitle_example�subsection_examplerV   Z
LabelframeZ	codeFramer�   ZoutputFrameZaddressFrameZ	flowFrameZ
notesFrame�Text�codeText�
outputTextZvarFrameZvalFrame�varData�valDataZSpinbox�flowControl�	notesTextr�   ZbackTOC_exampleZprevPage_exampleZnextPage_exampler�   r�   r�   r�   rY   rI   rJ   r3   r4   r5   r`   r6   rK   rL   rH   ry   r7   r8   r9   r:   r�   r~   )rc   Zhspecialrf   rf   rg   r�   �  s�    







zbasicLearning.createEXAMPLEc                 C   sZ   | j }| j�|�}| j��  |dkr>| jjdtd� | ��  n| j|d  | _ | �	�  d S r�   )
r�   r�   r�   r�   r�   r_   r`   ra   r�   r�   r�   rf   rf   rg   r~   J  s    

z'basicLearning.prevPage_example_callbackc                 C   s<   | j }| j�|�}| j|d  }|| _ | j��  | ��  d S r�   )r�   r�   r�   r�   r�   r�   r�   rf   rf   rg   r�   U  s    
z'basicLearning.nextPage_example_callbackc                 C   s&   | j ��  | jjdtd� | ��  d S r�   )r�   r�   r_   r`   ra   r�   r�   rf   rf   rg   ry   ]  s    
z&basicLearning.backTOC_example_callbackc                 C   s�  | j }| j| d s | ��  �n\| jjdd� t� | _t� | _t� | _t� | _	| j�
dd� | j�
dd� | j�
dd� | j�
dd� | j�
dd� | j�d� | j| }| jjdtd� | jj|d	 d
� | jj|d d
� | jj|d d
� | �| j| � ttdt| j�d ��}|��  | jj|dd� | jj| jd� | ��  | �| j| � | ��  | ��  | jjdd� d| _ d S )Nr�   r   �r�   �1.0�endr   Tr   r�   r�   r�   r�   g      �)�valuesZ	incrementr�   r�   rk   )!r�   r�   r�   r�   r�   �list�lineNum�varDictr�   �args�deleter   r  r  r  r  �setr�   r`   ra   r�   r�   r�   �analyzeCode�funcDict�range�len�reverse�changeIndex�loadCode�captureOutput�buildCapListrb   )rc   r�   r�   ZvalListrf   rf   rg   r�   b  s>    
zbasicLearning.loadExamplec                    s�   � �fdd��t ��� |�  t �d � � jd � j }t|d�}|�� }|��  |� jd � }tt	� j
d d � j
d ��}t� � _|D ]}� j�|| � q�t	t� j
��D ]}� j
| |d  � j
|< q�d S )Nc                    s�   t | j�}d|kr|d= � j�|� � j�| j� � j�|� � j�|� |dkr\| jj� _	� jt
� j�d  dkr�� j	� jd< �S )Nrc   �returnr   �����)�dict�f_localsr  �appendr
  �f_linenor�   r  �f_backZ
lastCalledr  )�framer�   r  ZtempDict�rc   �trace_callbackrf   rg   r!  �  s    

z1basicLearning.analyzeCode.<locals>.trace_callback�/r   r   �����r   )�sys�settracer'   r)   r+   �	readlinesr-   r*   r	  r  r
  �coder  r  )rc   �foor"   r   rd   ZcodeInds�irf   r   rg   r  �  s    


zbasicLearning.analyzeCodec                 C   s�  | j }| jjdd� | jjdd� | jjdd� | jjdd� | jt| j�	� � }t|�}t| j�	� �dk�rd}| j
�td�td�d td�d � | j
jtd�| jd� tdt| j�d �D ]<}| j
�t|�t|�d t|�d � | j
jt|�d	d� q��n�| jt| j�	� �d  }||k�r�td|�D ]>}| j
�t|�t|�d t|�d � | j
jt|�d	d� �q.| j
�t|�t|�d t|�d � | j
jt|�| jd� t|d |�D ]>}| j
�t|�t|�d t|�d � | j
jt|�d	d� �q�| j
�t|�t|�d t|�d � | j
jt|�| jd� t|d t| j�d �D ]>}| j
�t|�t|�d t|�d � | j
jt|�d	d� �qH�ndtd|�D ]>}| j
�t|�t|�d t|�d � | j
jt|�d	d� �q�| j
�t|�t|�d t|�d � | j
jt|�| jd� t|d |�D ]>}| j
�t|�t|�d t|�d � | j
jt|�d	d� �q| j
�t|�t|�d t|�d � | j
jt|�| jd� t|d t| j�d �D ]>}| j
�t|�t|�d t|�d � | j
jt|�d	d� �q�t| jt| j�	� � �� �}| j�d
d� | j�d
d� tt|��D ]�}| j�t|d �d t|| d �d � t|| d �}|d d� dk�r�|�d�td� }|d d� d ||d �  }| j�t|d �d |d � �q4| j�d
d� tt| j�	� ��D ].}| j| dk�r�| j�d| j| d � �q�| jjdd� | jjdd� | jjdd� t| j�	� �}| j�d
d� || j| k�r�| j�d
| j| | � | jjdd� d S )Nr   r  r   �d   �.0z.end)r�   r�   � r  r  r   r   �	   z	<functionz	<locals>.� �STEP!!!STEPr�   )r�   r   r�   r  r  r  r
  �intr  �getr�   �tag_addr1   �tag_configurerU   r  r  r'  rT   r	  r  �itemsr  �insert�find�captureListr�   )rc   r�   �valZlastValr)  ZdictList�valuer�   rf   rf   rg   r  �  s�    $$
$$$$$$$$$$*"zbasicLearning.changeIndexc              	      sP   t �� }t|��, � fdd�� t�� � |�  t�d � W 5 Q R X |�� | _d S )Nc                    s   t d� � S )Nr/  �rV   )r  r�   r  ��capture_callbackrf   rg   r<  �  s    z5basicLearning.captureOutput.<locals>.capture_callback)�io�StringIOr   r$  r%  �getvalue�capture)rc   r(  �frf   r;  rg   r  �  s    

zbasicLearning.captureOutputc                 C   s�   d}| j }t� }|dkrR|�d�}|dkrR|�|d |� � nqR||d d � }qt� | _tt|�d �D ]$}||d  dkrj| j�|| � qjd S )Nr   r  r   r/  )r@  r	  r6  r  r7  r  r  )rc   r�   �stringr7  r)  rf   rf   rg   r  �  s    
zbasicLearning.buildCapListc                 C   sF   d}|dkrB|� d�}|dkr qB|d |� d ||d d �  }q|S )Nr   r  �	z    )r6  )rc   rB  r�   rf   rf   rg   �replaceTabs
  s    
"zbasicLearning.replaceTabsc                 C   s�   t t| j��D ]r}t|d �d }| j| dd � }| �|�}|t| j�d krbd�|d |�}nd�|d d�}| j�||� qd S )Nr   r+  r�   z
{:02d}  {}z#EOF)r  r  r'  r1   rD  �formatr�   r5  )rc   r)  r�   rB  rf   rf   rg   r    s    
zbasicLearning.loadCodec                 C   s�  t �| j�| _t �| j�| _t �| j�| _t �| j�| _| jdkr�t �| j�| _	t �| j�| _
t �| j�| _t �| j�| _d}nH| jdkr�t| j�| _	t| j�| _
t| j�| _t| j�| _d}ntd� t| jdd�| _t| jdd�| _t| jd	d�| _t| j�| _t| j�| _t| j�| _t| j�| _t| j�| _t| j�| _| jjd
d
d� | jjddd� | jjdd
d� | jjd
dd� | jjd
d
dd� | jjdd
dd� | jjdd
dd� | jjd
dd� | jjddd� | jjddd� | jjd
dd� | jjddd� | jjd
dd� | jjddd� | jjddd� | jjd
dd� | jjd
dd� | jjd
dd� | jjddd� | jjddd� | jjdd� | jjd
d
d� | j	jd
d
ddd� | j
jd
ddd� | jjdddd� | jjdddd� | j	j| j| j| j d� | j
j| j!| j| j ddd� | jj| j"| j| j ddd� | jj| j#| j| j ddd� | jjd
d
dd� | jjdd
dd� | jjdd
dd� | jj| j$| j%d� | jj| j&| j'd� | jj| j(| j)d� | jj*ddd� | jj*ddd� | jj*ddd� | jjd|d� | jjd|d� | jjd|d� | jjd| j+d � | jjd| j,d � | jjd| j-d � | jjd
d
d!d� | jjd
dd!d� | jjd
dd!d� | jdk�r | jjd"| j.| j/| j0| j1d#� | jjd$| j.| j/| j0| j1d#� | jjd%| j.| j/| j0| j1d#� np| jdk�rh| jjd"| j.| j/| j0| j1d&� | jjd$| j.| j/| j0| j1d&� | jjd%| j.| j/| j0| j1d&� ntd� | jj| j2d'� | jj| j3d'� | jj| j4d'� d S )(Nr   r*  r   �n   r   zKnowledge and Understandingr�   zThinking and InquiryzApplication and Communicationr   r�   r   r�   r�   r�   r�   r�   r�   Znswr�   r�   r�   r	   r�   �r�   r�   T�yr   r�   )r�   r�   rq   )r�   r�   r�   r�   r�   r�   r�   r�   r�   )5r   r�   r/   �practiceFrameZhead_practiceZbody_practiceZfoot_practicer    r�   Zlogo_practice�title_practice�subtitle_practice�subsection_practicerV   r�   ZkuFrameZtiFrameZaFramer�   �kuText�tiText�aTextr�   ZbackTOC_practiceZprevPage_practiceZnextPage_practicer�   r�   r�   r�   rY   rI   rJ   r3   r4   r5   rM   rN   rO   rP   rQ   rR   r`   rC   rD   rE   r6   rK   rL   rH   rz   r�   r   �rc   �widrf   rf   rg   r�      s�    

  zbasicLearning.createPRACTICEc                 C   sZ   | j }| j�|�}| j��  |dkr>| jjdtd� | ��  n| j|d  | _ | �	�  d S r�   )
r�   r�   r�   rI  r�   r_   r`   ra   r�   r�   r�   rf   rf   rg   r   �  s    

z(basicLearning.prevPage_practice_callbackc                 C   s<   | j }| j�|�}| j|d  }|| _ | j��  | ��  d S r�   )r�   r�   r�   rI  r�   r�   r�   rf   rf   rg   r�   �  s    
z(basicLearning.nextPage_practice_callbackc                 C   s�  | j }| j| }| j| d s*| ��  �n�| jjdd� | jjdd� | jjdd� | jjdt	d� | j
j|d d� | jj|d d� | jj|d	 d� | j�d
d� | j�d
| j| d � | j�dd
d� | jjd| jd� | jj| j| d d� | j�d
d� | j�d
| j| d � | j�dd
d� | jjd| jd� | jj| j| d d� | j�d
d� | j�d
| j| d � | j�dd
d� | jjd| jd� | jj| j| d d� | jjdd� | jjdd� | jjdd� d| _d S )Nr�   r   r  Tr   r�   r�   r�   r�   r  r  �KUZkutagr�   �kuHeight�r�   �TIZtitag�tiHeight�AZatag�aHeightr�   rl   )r�   r�   r�   rM  r�   rN  rO  rI  r`   ra   rJ  rK  rL  r  r5  r2  r3  r@   rA   rB   rb   r�   rf   rf   rg   r�   �  s>    
zbasicLearning.loadPracticec                 C   s&   | j ��  | jjdtd� | ��  d S r�   )rI  r�   r_   r`   ra   r�   r�   rf   rf   rg   rz   �  s    
z'basicLearning.backTOC_practice_callbackc                 C   sF  t �| j�| _t �| j�| _t �| j�| _t �| j�| _| jdkr�t �| j�| _	t �| j�| _
t �| j�| _t �| j�| _d}nH| jdkr�t| j�| _	t| j�| _
t| j�| _t| j�| _d}ntd� t �| j�| _t| j�| _t| j�| _t| j�| _| jjddd� | jjddd� | jjd	dd� | jjddd� | jjddd
d� | jjddd
d� | jjd	dd
d� | jjddd� | jjddd� | jjd	dd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjddd� | jjd	dd� | jjdd� | j	jddddd� | j
jddd
d� | jjddd
d� | jjd	dd
d� | j	j| j| jd� | j
j| j| j| jddd� | jj| j| j| jddd� | jj| j| j| jddd� | jjddd� | jj|d| jd� | jjdddd� | jjdddd� | jjdd	dd� | jdk�r�| jjd| j| j| j | j!d� | jjd| j| j| j | j!d� | jjd| j| j| j | j!d� np| jdk�r
| jjd| j| j| j | j!d� | jjd| j| j| j | j!d� | jjd| j| j| j | j!d� ntd� | jj| j"d� | jj| j#d� | jj| j$d� d S )Nr   �A   r   �P   r   r   r�   r   r�   r�   r�   r�   r�   r�   Znwsr�   r�   r�   r	   r�   r�   i�  )r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   )%r   r�   r/   �projectFrameZhead_projectZbody_projectZfoot_projectr    r�   Zlogo_project�title_project�subtitle_project�subsection_projectrV   �projectTextr�   ZbackTOC_projectZprevPage_projectZnextPage_projectr�   r�   r�   r�   rY   rI   r3   rJ   r4   r5   r?   r6   rK   rL   rH   r{   r�   r�   rP  rf   rf   rg   r�   �  s�    

  zbasicLearning.createPROJECTc                 C   sZ   | j }| j�|�}| j��  |dkr>| jjdtd� | ��  n| j|d  | _ | �	�  d S r�   )
r�   r�   r�   r[  r�   r_   r`   ra   r�   r�   r�   rf   rf   rg   r�     s    

z'basicLearning.prevPage_project_callbackc                 C   s<   | j }| j�|�}| j|d  }|| _ | j��  | ��  d S r�   )r�   r�   r�   r[  r�   r�   r�   rf   rf   rg   r�   %  s    
z'basicLearning.nextPage_project_callbackc                 C   sx   | j }| j| }| jjdtd� | jj|d d� | jj|d d� | jj|d d� | j	j| j| d d� d| _
d S )	NTr   r�   r�   r�   r�   r�   rm   )r�   r�   r[  r`   ra   r\  r�   r]  r^  r_  rb   r�   rf   rf   rg   r�   -  s    
zbasicLearning.loadProjectc                 C   s&   | j ��  | jjdtd� | ��  d S r�   )r[  r�   r_   r`   ra   r�   r�   rf   rf   rg   r{   8  s    
z&basicLearning.backTOC_project_callbackc                 C   s�  t �| j�| _t �| j�| _t �| j�| _t �| j�| _| jdkrdt �| j�| _	t �| j�| _
d}n0| jdkr�t| j�| _	t| j�| _
d}ntd� t| jdd�| _t �| j�| _t �| j�| _t| j�| _| jjddd	� | jjd
d
d	� | jjddd	� | jjdd
d	� | jjdddd� | jjd
ddd� | jjdddd� | jjdtd� | jjdd� | jjdd� | jjd| jdd� | jjdd
d	� | jjd
d
d	� | jjdd
d	� | jjd
d
d	� | j	j| j| jd� | j	jddddd� | j
jd| jd� | j
jdd
d
ddd� | j
j| j| jd� | j
j| j| jdd� | jjddd� | jjdd � | jjdd � d!}| jjd|d"� | jjd|d"� | jjdddd� | jjdd
dd� | jj|d#� | jj|d#� | jjdd
d	� | jjdd
d	� | jjdddd� | jj| j | j| j!d$d%� | jdk�r:| jj| j"| j#d&� n*| jdk�r\| jj| j"| j#d'� ntd� | jjd(d)� | jjd(d)� | �$�  | j�%d*| j&� | j�%d*| j'� | j�%d+| j(� | jj| j)d,� | j�%d-| j*� | j�%d.| j+� | j�,�  d S )/Nr   �   r   r   r   zTable of Contentsr�   r   r�   r   r�   r�   r�   Tr   r�   r�   rq   r�   )r�   r�   r�   r�   r�   zPython Programming
The Basicsr�   )r�   r�   r�   r�   r�   )r�   r�   r�   )r�   r�   r�   �#0ZCHAPTERSZtree)Zshowi�  )r�   rT  r   )r�   r�   r�   r�   rG  )r�   r�   Zbrowse)Z
selectmodez<<TreeviewSelect>>z<<TreeviewOpen>>r�   z<Double-Button-1>z<Return>)-r   r�   r/   r_   Zhead_tocZbody_tocZfoot_tocr    r�   Zlogo_tocZ	title_tocrV   r�   Z
toc_lFrameZTreeview�tocLEFT�tocRIGHTr�   �loadPager�   r�   r�   r`   ra   r�   r;   rX   rI   rJ   r2   �headingr�   rH   rG   rK   rL   �initializeTOCrZ   �tocLEFT_callback�tocRIGHT_callback�closeTrees_callbackr�   �mouse�enterPressedZ	focus_set)rc   ZnrowsZtreeWidrf   rf   rg   r�   >  s�    

zbasicLearning.createTOCc                 C   s>   | � �  | j�| j�}| jj|dd� | j�| j� d| _d S )NT�r+   r   )�
closeTreesrc  �parentr�   �item�selection_setrb   )rc   rn  rf   rf   rg   r�   �  s
    zbasicLearning.prepareTOCc                 C   s�   d}| j ��  | �| j� | j| dkr2| ��  nP| j| dkrJ| ��  n8| j| dkrb| ��  n | j| dkrz| ��  ntd� d S )Nrs   ro   rt   ru   rv   rw   )	r_   r�   �writeLastPager�   r�   r�   r�   r�   rV   )rc   r�   rf   rf   rg   r�   �  s    




zbasicLearning.loadPage_callbackc                 C   s,   | j �� d }t|�dkr(|| _| ��  d S �Nr   r-  �rc  �	selectionr  r�   r�   �rc   r�   r�   rf   rf   rg   rk  �  s    zbasicLearning.enterPressedc                 C   s,   | j �� d }t|�dkr(|| _| ��  d S rr  rs  ru  rf   rf   rg   rj  �  s    zbasicLearning.mousec                 C   s�  t t| jd ��D ]4}| jjdt|�dt|d � | jd | dd� q| jjddd� t� | _t t| jd ��D ]}| j�	t� � | �
|� qrt| jd	 d
�}|�� }|��  |d }|�d�d }|�d�d }t|||d � �d }t|||d � �d }| �|� | j�� | }	| j�� | }
| j�|	� | jj|
dd� | j�|� | �|� | j�| j�� d�}| jjd|d� d S )Nr   r,  r�   r   Zchfont�r�   Ztags��Calibrir   r   r�   �lastPageViewed.txtr   �c�sr�   Trl  r�   ra  r�   )r  r  �tocDatarb  r5  r1   r3  r	  �toc_sectionIDr  �buildSectionTreer+   r&   r&  r-   r6  r0  �reattach_TOC�get_childrenrc  rp  ro  �loadPage_textrt  re  )rc   r)  r   �linesZFULL_ID�cInd�sIndZc_indexZs_indexZCHAP_IDZSECT_IDrB  rf   rf   rg   rf  �  s2    2

zbasicLearning.initializeTOCc                 C   s"  |� d�d }|� d�d }d|kr8|� d�d }d}n\d|krT|� d�d }d}n@d|krp|� d�d }d	}n$d
|kr�|� d
�d }d}nd}d}|r�d|||d �  d |||d �  d | ||d �  }n4d|||d �  d |||d �  d | d }| jj|d� || _d S )Nrz  r   r{  ro   zLesson rt   zExample ru   zReview rv   zProject FzLOAD: Chapter r�   z
, Section z, Z01r�   )r6  rd  r�   r�   )rc   r�   r�  r�  ZlastInd�suffixrB  rf   rf   rg   r�  �  s*    >4zbasicLearning.loadPage_textc                 C   s6   t t| j| ��D ]}| j�| j| | d|� qd S )Nr,  )r  r  r}  rc  Zmove)rc   r�   r)  rf   rf   rg   r  �  s    zbasicLearning.reattach_TOCc           	      C   s�   | j �� }tt|��D ]}| j �|| � q| j�� d }| j�|d�}| j jd|d� | j�	|�}| �
|� | j �� }| js�| ��  | j �|d �d }|| _| ��  | �|� nd| _d S )Nr   r�   ra  r�   F)rc  r�  r  r  �detachrb  rt  ro  re  r�   r  r\   rm  r�   r�   r�  )	rc   r�   �childrenr)  r�   rB  r�   Z	rChildrenZchildrf   rf   rg   rg  �  s"    


zbasicLearning.tocLEFT_callbackc                 C   s0   | j �� d }t|�dkr"|d }| �|� d S )Nr   r�   Zp01)rc  rt  r  r�  ru  rf   rf   rg   rh    s
    
zbasicLearning.tocRIGHT_callbackc           
      C   s�  d}t t| jd | ��D �]h}d| jd | | kr�|d }d}d}d}d}d�|d |�}| j| �|� | jjdt|�|| jd | | dd� | j�	|� qd| jd | | kr�|d }|d	�|� }	n�d
| jd | | k�r|d }|d�|� }	n^d| jd | | k�r2|d }|d�|� }	n.d| jd | | k�r`|d }|d�|� }	| jj|d|	| jd | | dd� q| jj
ddd� | jj
ddd� d S )Nr   r   �Sectionzc{:02d}s{:02d}r,  ZsecFontrv  �Lessonzp{:02d}�Exampleze{:02d}�Reviewzh{:02d}�Projectzm{:02d}r  ZpgFontrw  r�   )rx  r�   r   )r  r  r|  rE  r}  r  rc  r5  r1   r�  r3  )
rc   r�   Zsind�jZpindZeind�hindZmindZcurIDr�   rf   rf   rg   r~    s8    (&zbasicLearning.buildSectionTreec                 C   s   | � �  d S r�   )rm  r�   rf   rf   rg   ri  ,  s    z!basicLearning.closeTrees_callbackc                 C   s4   | j �� }tt|��D ]}| j j|| dd� qd S )NFrl  )rc  r�  r  r  ro  )rc   r�  r)  rf   rf   rg   rm  /  s    
zbasicLearning.closeTreesc                 C   s   | � �  | ��  | ��  d S r�   )�loadTOC�loadPageData�loadFuncDictr�   rf   rf   rg   r]   6  s    zbasicLearning.loadProgramDatac                 C   s�  t � | _t� | _t� | _t� | _t� | _tt| j	d ��D �]2}d}tt| j	d | ��D �]}d}| j	d | | �
d�}d|kr�|d }d}d}d}d}	d}|}
d|kr�d}|d }|}nXd	|kr�d
}|d }|}n>d|kr�d}|d }|}n$d|k�rd}|	d }	|	}nd}d}|rZd�|d |||�}| j�|� d| j	d |  d }d|
 d }d| d }|dk�r�t� | j|< || j| d< || j| d< || j| d< qZ|d
k�r�t� | j|< || j| d< || j| d< || j| d< qZ|dk�r.t� | j|< || j| d< || j| d< || j| d< qZ|dkrZt� | j|< || j| d< || j| d< || j| d< qZq:tt| j��D ]8}| j| j|  d }tj�|�}| �| j| |� �q~d S )Nr   r   Tr   r�  Fr�  ro   r�  rt   r�  ru   r�  rv   �errorzc{:02d}s{:02d}{}{:02d}�  r�   r�   r�   �.txt)r	  r�   r  r�   r�   r�   r�   r  r  r|  r�   rE  r  r'   r!   r"   �exists�
loadIDdata)rc   r)  r�  r�  ZdoAppend�entryZpIndZeIndZhIndZmIndZsectionName�charr�   rB  Z	chapTitleZsecTitleZ	pageTitle�filename�	fileFoundrf   rf   rg   r�  ;  s�    



zbasicLearning.loadPageDatac                 C   sn   d}|| dkr| � ||� nL|| dkr8| �||� n2|| dkrR| �||� n|| dkrj| �||� d S )Nr�   ro   rt   ru   rv   )�loadLessonData�loadExampleData�loadPracticeData�loadProjectData)rc   r�   r�  r�   rf   rf   rg   r�  �  s    zbasicLearning.loadIDdatac                 C   sj   || j | d< |rft| j| d �}|�� }|��  d}tdt|��D ]}|||  }qF|| j | d< d S )Nr�   r�  r,  r   r�   )r�   r+   r'   r&  r-   r  r  )rc   r�   r�  r   r�  rB  r)  rf   rf   rg   r�  �  s    zbasicLearning.loadProjectDatac           
      C   s�  || j | d< |�r�t| j| d �}|�� }|��  tt|��D ]�}d|| kr�|| �d�d }t|| |d � �	d��| j | d< qBd|| kr�|}|| �d�d }t|| |d � �	d��| j | d	< qBd
|| krB|}|| �d�d }t|| |d � �	d��| j | d<  �q qBd}	td|�D ]}|	||  }	�q.|	�	d�| j | d< d}	t|d |�D ]}|	||  }	�qh|	�	d�| j | d< d}	t|d t|��D ]}|	||  }	�q�|	�	d�| j | d< d S )Nr�   r�  z#KU#ru   r   r   rS  z#TI#rV  z#A#rX  r,  rR  rU  rW  )
r�   r+   r'   r&  r-   r  r  r6  �floatr�   )
rc   r�   r�  r   r�  r)  r�  Zind1Zind2rB  rf   rf   rg   r�  �  s>    &&$zbasicLearning.loadPracticeDatac           	      C   s�   || j | d< |r�t| j| d �}|�� }|��  | j|d �d� }t|d�}|| j | d< |d | j | d< d	}td
t	|��D ]}|||  }q�|| j | d< d S )Nr�   r�  r   r   r   r�   r�   r�   r,  �   r�   )
r�   r+   r'   r&  r-   r(   r�   rW   r  r  )	rc   r�   r�  r   r�  ZimPathZimrB  r)  rf   rf   rg   r�  �  s    
zbasicLearning.loadLessonDatac                 C   s�   || j | d< |r�t| j| d �}|�� }|��  t� }tt|��D ]}d|| krF|�|� qFtt|�d �D ]j}|||  }t	|dd � �
d��}d}	t|| d ||d  �D ]}
|	||
  }	q�|	�
d�| j | |< qrd S )Nr�   r�  z#n#r   r�   r   r,  )r�   r+   r'   r&  r-   r	  r  r  r  r0  r�   )rc   r�   r�  r   r�  Zindlistr)  �liner�   Znoter�  rf   rf   rg   r�  �  s"    zbasicLearning.loadExampleDatac                 C   st  t | jd d�}|�� }|��  d|kr4|�d� q t� }tt|��D ]"}|| dd� dkrF|�|� qFt� | _	| j	�t� � | j	�t� � td|d �D ]}| j	d �|| �
d�� q�tt|�d �D ]T}| j	d �t� � t|| d ||d  �D ]"}| j	d | �|| �
d�� q�q�| j	d �t� � t|d	 d t|��D ]$}| j	d d	 �|| �
d�� �qJd S )
NztocData.txtr   r   r   r�   z#cr   z\	nr  )r+   r&   r&  r-   �remover	  r  r  r  r|  r�   )rc   r   r�  Zindsr)  r�  rf   rf   rg   r�  �  s,    ""zbasicLearning.loadTOCc                 C   s&   t | jd d�}|�|� |��  d S )Nry  r	   )r+   r&   r.   r-   )rc   r�   r   rf   rf   rg   rq  �  s    
zbasicLearning.writeLastPagec                 C   s  t � | _| j| jd< | j| jd< | j| jd< | j| jd< | j| jd< | j| jd< | j| jd< | j	| jd< | j
| jd	< | j| jd
< | j| jd< | j| jd< | j| jd< | j| jd< | j| jd< | j| jd< | j| jd< | j| jd< | j| jd< | j| jd< | j| jd< | j| jd< d S )N�	c01s03e01�	c01s03e02�	c01s03e03�	c02s01e01�	c02s01e02�	c02s01e03�	c02s01e04�	c02s03e01�	c02s03e02�	c02s03e03�	c02s03e04�	c03s01e01�	c03s02e01�	c04s01e01�	c04s01e02�	c04s01e03�	c04s02e01�	c04s02e02�	c04s02e03�	c05s01e01�	c05s01e02�	c05s01e03)r  r  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�   rf   rf   rg   r�    s.    zbasicLearning.loadFuncDictc                 C   sL   d}t |�}d}t |�}d}t |�}d}t |�}d}t |�}d}t |�}d S )Nr�   ZhelloTr�  �hello thereF��id)rc   r
   �addressXrH  �addressY�zZaddressZrf   rf   rg   r�  %  s    zbasicLearning.c01s03e01c                 C   s(   d}t |�}|}t |�}d}t |�}d S )Nr�   r�   r�  )rc   r
   r�  rH  r�  rf   rf   rg   r�  4  s    zbasicLearning.c01s03e02c                 C   s   d}d}d}t |� d S )Nr�  zsay it ain't sozyou're quite welcomer:  )rc   r
   rH  r�  rf   rf   rg   r�  =  s
    zbasicLearning.c01s03e03c           	      C   sT   d}d}t |�}t |�}t|�}t|�}t |�}t |�}td| � td| � d S )Nr   g      $@zn1 has value zn2 has value )�typer1   rV   )	rc   �n1�n2ZtypeN1�typeN2�s1�s2�typeS1�typeS2rf   rf   rg   r�  D  s    zbasicLearning.c02s01e01c                 C   sL   d}d}t |�}t |�}t|�}t|�}t|�}t |�}t |�}	t |�}
d S )NZ10z10.0)r�  r0  r�  )rc   r�  r�  r�  r�  Zn1aZn1br�  ZtypeN1AZtypeN1Br�  rf   rf   rg   r�  Q  s    zbasicLearning.c02s01e02c                 C   s   d}d}t |�}t |�}d S )Nzhello worldz    spaces are characters too    )r  )rc   r�  r�  ZL1ZL2rf   rf   rg   r�  ^  s
    zbasicLearning.c02s01e03c           	      C   s4   d}d}d}d}t |�}t |�}t |�}t |�}d S )Ni����r   g{�G�z@g{�G�z�)�abs)	rc   r�  r�  Zn3Zn4ZabsN1ZabsN2ZabsN3ZabsN4rf   rf   rg   r�  e  s    zbasicLearning.c02s01e04c                 C   s2   dd� }|dd�}|dd�}d}d}|||�}d S )Nc                 S   s   | | }|S r�   rf   )Znum1Znum2�resultrf   rf   rg   r(  q  s    z$basicLearning.c02s03e01.<locals>.foor�   r�   r�   �   r�   rf   )rc   r(  Zanswer1Zanswer2r�  r�  Zanswer3rf   rf   rg   r�  p  s    


zbasicLearning.c02s03e01c                 C   s    dd� }|�  t d� |�  d S )Nc                   S   s,   t d� t d� t d� t d� t d� d S )N�  |   |   |  �  |   o   |  �  |  \|/  |  �  |  / \  |  r:  rf   rf   rf   rg   r(  |  s    z$basicLearning.c02s03e02.<locals>.foo�~~~~~~~~~~~~~r:  �rc   r(  rf   rf   rg   r�  {  s
    zbasicLearning.c02s03e02c                 C   s(   dd� }|dd� t d� |dd� d S )Nc                 S   s�   t d| d | d |  � t d| d | d |  � t d| d | d |  � t d| d | d |  � t d| d | d |  � d S )Nr�  z   |   z   o   z  \|/  z  / \  r:  )rQ  r�  rf   rf   rg   r(  �  s    z$basicLearning.c02s03e03.<locals>.foor�   �#z4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~r�   �:r:  r�  rf   rf   rg   r�  �  s
    

zbasicLearning.c02s03e03c                 C   s"   dd� }|� }t d� t |� d S )Nc                   S   s,   t d� t d� t d� t d� t d� dS )Nr�  r�  r�  r�  zA HANGMAN WAS PRINTED TO SCREENr:  rf   rf   rf   rg   r(  �  s    z$basicLearning.c02s03e04.<locals>.foor�  r:  )rc   r(  Z	exitValuerf   rf   rg   r�  �  s
    zbasicLearning.c02s03e04c           	      C   sp   t d�d d  t d�d d }tt d�d d � td�td� }td�}td�d }td�}d}d}d	}d S )
N�hir�  r   r�   r�   g       @�2Z22222g      A@)r  rV   r0  )	rc   r
   Zval1Zval2Zval3Zval4ZquotientZ	remainderZ	randomValrf   rf   rg   r�  �  s    zbasicLearning.c03s01e01c                 C   s�   d}|d |d  |d  |d  }|d |d  |d  |d	  |d
  }|d |d  |d  |dd�  }|d d� }|dd � }t d| | d � t || |d  | � d S )NzAlbert Einsteinr�  r�   r  r�   �   r   r#  �����rs   r�   r�   r   r�  r�   zAnagram of z is: r:  )rc   �nameZpt1Zpt2Zpt3Z	firstNameZlastNamerf   rf   rg   r�  �  s     ($zbasicLearning.c03s02e01c                 C   s\   d}d}||kr(t d� t d� t d� t d� ||k rPt d� t d� t d� t d� d S )Nr�   r�   z------------------�x is larger than yzRandom Message #1�x is less than yzRandom Message #2r:  �rc   r
   rH  rf   rf   rg   r�  �  s    zbasicLearning.c04s01e01c                 C   sP   d}d}||krt d� nt d� t d� ||kr<t d� nt d� t d� d S )Nr�   r�   �x is equal to yzx is not equal to yzDone first test!zx is not equal to y .. againzDone second test!r:  r�  rf   rf   rg   r�  �  s    

zbasicLearning.c04s01e02c                 C   sX   d}d}||kr"t d� t d� n*||kr<t d� t d� nt d� t d� t d� d S )	Nr�   r�  zrandom message #1r�  zrandom message #2r�  zrandom message #3zrandom message #4r:  r�  rf   rf   rg   r�  �  s    

zbasicLearning.c04s01e03c                 C   s6   d}|}|dkr*t t|�d � |d }qt d� d S )Nr   r   �..r   z
Blast Off!)rV   r1   �rc   rr   r)  rf   rf   rg   r�  �  s    
zbasicLearning.c04s02e01c                 C   s>   d}t |�D ]}tt|d �d � qtdt|� d � d S )Nr   r   r�  zCounted to �!)r  rV   r1   r�  rf   rf   rg   r�  �  s
    zbasicLearning.c04s02e02c                 C   sT   t d� tddd�D ]2}|d dkr6t t|�d � qt t|�d � qt d� d S )Nz
----------r�   r   r�  r   z is a multiple of 8z is not a multiple of 8)rV   r  r1   )rc   r)  rf   rf   rg   r�  �  s    zbasicLearning.c04s02e03c                 C   sT   d}t |� d}|dkrH|�d�}|dkr|d |� ||d d �  }qt |� d S �NzThis string has i's in itr�   r  r)  r   �rV   r6  �rc   Zstring1r�   rf   rf   rg   r�    s    
zbasicLearning.c05s01e01c                 C   sT   d}t |� d}|dkrH|�d�}|dkr|d |� ||d d �  }qt |� d S r�  r�  r�  rf   rf   rg   r�    s    
zbasicLearning.c05s01e02c                 C   sT   d}t |� d}|dkrH|�d�}|dkr|d |� ||d d �  }qt |� d S r�  r�  r�  rf   rf   rg   r�    s    
zbasicLearning.c05s01e03N)Q�__name__�
__module__�__qualname__rh   r[   r^   r�   r�   r�   r|   r�   r}   r�   rx   r�   r�   r~   r�   ry   r�   r  r  r  r  rD  r  r�   r   r�   r�   rz   r�   r�   r�   r�   r{   r�   r�   r�   rk  rj  rf  r�  r  rg  rh  r~  ri  rm  r]   r�  r�  r�  r�  r�  r�  r�  rq  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  rf   rf   rf   rg   r      s�    /
I	_ "!G	i&RQ I!"		
r   )r$  r!   Ztkinterr   �
contextlibr   r=  r   ZTkr/   ZGUIZmainlooprf   rf   rf   rg   �<module>   s.                 %