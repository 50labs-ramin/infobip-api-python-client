# coding: utf-8

"""
    Infobip Client API Libraries OpenAPI Specification

    OpenAPI specification containing public endpoints supported in client API libraries.

    The version of the OpenAPI document: 1.0.0
    Contact: support@infobip.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class CallVoice(str, Enum):
    """
    Voice name in which text would be synthesized. More info about available languages and voices can be found [here](https://www.infobip.com/docs/voice-and-video/getting-started#text-to-speech).
    """

    """
    allowed enum values
    """
    ZEINA = "Zeina"
    AISHA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Aisha (beta)"
    FAROOQ_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Farooq (beta)"
    HUSSEIN_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Hussein (beta)"
    AMAL_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Amal (beta)"
    SAYAN_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Sayan (beta)"
    SUSHMITA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Sushmita (beta)"
    DARINA = "Darina"
    CONCHITA = "Conchita"
    ZHIYU = "Zhiyu"
    LIU_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Liu (beta)"
    WANG_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Wang (beta)"
    ZHANG_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Zhang (beta)"
    LIN_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Lin (beta)"
    AKEMI_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Akemi (beta)"
    CHEN_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Chen (beta)"
    HUANG_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Huang (beta)"
    FANG = "Fang"
    CHAO = "Chao"
    MING = "Ming"
    ANETA = "Aneta"
    NAJA = "Naja"
    MADS = "Mads"
    RUBEN = "Ruben"
    LOTTE = "Lotte"
    JOANNA = "Joanna"
    IVY = "Ivy"
    KENDRA = "Kendra"
    KIMBERLY = "Kimberly"
    SALLI = "Salli"
    JOEY = "Joey"
    JUSTIN = "Justin"
    MATTHEW = "Matthew"
    RUSSELL = "Russell"
    NICOLE = "Nicole"
    BRIAN = "Brian"
    AMY = "Amy"
    EMMA = "Emma"
    ADITI = "Aditi"
    RAVEENA = "Raveena"
    GERAINT = "Geraint"
    EVELIN_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Evelin (beta)"
    CELINE = "Celine"
    LEA = "Lea"
    MATHIEU = "Mathieu"
    CHANTAL = "Chantal"
    VICKI = "Vicki"
    HANS = "Hans"
    MARLENE = "Marlene"
    SOPHIA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Sophia (beta)"
    DINESH_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Dinesh (beta)"
    LEELA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Leela (beta)"
    ABIGAIL = "Abigail"
    MEIRA = "Meira"
    IDAN = "Idan"
    YOSEF = "Yosef"
    AADITA = "Aadita"
    AARUSHI_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Aarushi (beta)"
    AKASH_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Akash (beta)"
    DAMAN_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Daman (beta)"
    DIVYA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Divya (beta)"
    AGOTA = "Agota"
    DORA = "Dora"
    KARL = "Karl"
    INDAH_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Indah (beta)"
    ARIF_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Arif (beta)"
    REZA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Reza (beta)"
    NURUL_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Nurul (beta)"
    GIANNA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Gianna (beta)"
    CARLA = "Carla"
    BIANCA = "Bianca"
    GIORGIO = "Giorgio"
    TAKUMI = "Takumi"
    MIZUKI = "Mizuki"
    SHASHANK_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Shashank (beta)"
    NAMRATHA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Namratha (beta)"
    SEOYEON = "Seoyeon"
    SUMI_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Sumi (beta)"
    JINA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Jina (beta)"
    HIMCHAN_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Himchan (beta)"
    MINHO_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Minho (beta)"
    AMEERA = "Ameera"
    NURIN = "Nurin"
    NIJAT = "Nijat"
    FUAAD = "Fuaad"
    VISHNU_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Vishnu (beta)"
    KIRTI_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Kirti (beta)"
    LIV = "Liv"
    EWA = "Ewa"
    MAJA = "Maja"
    JACEK = "Jacek"
    JAN = "Jan"
    CRISTIANO = "Cristiano"
    INES = "Ines"
    ABRIELLE_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Abrielle (beta)"
    HENRIQUES_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Henriques (beta)"
    JERALDO_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Jeraldo (beta)"
    JACINDA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Jacinda (beta)"
    CAMILA = "Camila"
    RICARDO = "Ricardo"
    VITORIA = "Vitoria"
    CARMEN = "Carmen"
    MAXIM = "Maxim"
    TATYANA = "Tatyana"
    NATALIA = "Natalia"
    MIGUEL = "Miguel"
    LINDA = "Linda"
    ENRIQUE = "Enrique"
    GABRIELA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Gabriela (beta)"
    LUPE = "Lupe"
    PENELOPE = "Penelope"
    MIA = "Mia"
    ASTRID = "Astrid"
    GANESH_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Ganesh (beta)"
    SHRUTI_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Shruti (beta)"
    VIJAY_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Vijay (beta)"
    SAMANTHA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Samantha (beta)"
    NATCHAYA_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Natchaya (beta)"
    FILIZ = "Filiz"
    ULYANA = "Ulyana"
    LIEN_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Lien (beta)"
    QUAN_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Quan (beta)"
    MAI_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Mai (beta)"
    TUAN_LEFT_PARENTHESIS_BETA_RIGHT_PARENTHESIS = "Tuan (beta)"
    GWYNETH = "Gwyneth"
    AARYA = "Aarya"
    ARJUN = "Arjun"
    REVATI = "Revati"
    HAMED_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Hamed (neural)"
    SALMA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Salma (neural)"
    SHAKIR_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Shakir (neural)"
    ZARIYAH_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Zariyah (neural)"
    BASHKAR_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Bashkar (neural)"
    TANISHAA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Tanishaa (neural)"
    BORISLAV_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Borislav (neural)"
    KALINA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Kalina (neural)"
    ALBA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Alba (neural)"
    ENRIC_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Enric (neural)"
    JOANA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Joana (neural)"
    XIAOCHEN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaochen (neural)"
    XIAOHAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaohan (neural)"
    XIAOMENG_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaomeng (neural)"
    XIAOMO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaomo (neural)"
    XIAOQIU_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaoqiu (neural)"
    XIAOROU_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaorou (neural)"
    XIAORUI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaorui (neural)"
    XIAOXIAO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaoxiao (neural)"
    XIAOYAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaoyan (neural)"
    XIAOYI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaoyi (neural)"
    XIAOZHEN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Xiaozhen (neural)"
    YUNFENG_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yunfeng (neural)"
    YUNHAO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yunhao (neural)"
    YUNJIAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yunjian (neural)"
    YUNJIE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yunjie (neural)"
    YUNXI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yunxi (neural)"
    YUNXIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yunxia (neural)"
    YUNYANG_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yunyang (neural)"
    YUNYE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yunye (neural)"
    YUNZE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yunze (neural)"
    HIU_GAAI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "HiuGaai (neural)"
    HIU_MAAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "HiuMaan (neural)"
    HSIAO_CHEN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "HsiaoChen (neural)"
    HSIAO_YU_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "HsiaoYu (neural)"
    WAN_LUNG_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "WanLung (neural)"
    YUN_JHE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "YunJhe (neural)"
    GABRIJELA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Gabrijela (neural)"
    SRECKO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Srecko (neural)"
    ANTONIN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Antonin (neural)"
    VLASTA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Vlasta (neural)"
    CHRISTEL_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Christel (neural)"
    JEPPE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jeppe (neural)"
    COLETTE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Colette (neural)"
    FENNA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Fenna (neural)"
    MAARTEN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Maarten (neural)"
    AMBER_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Amber (neural)"
    ANDREW_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Andrew (neural)"
    ARIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Aria (neural)"
    ASHLEY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ashley (neural)"
    AVA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ava (neural)"
    BRANDON_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Brandon (neural)"
    BRIAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Brian (neural)"
    CHRISTOPHER_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Christopher (neural)"
    CORA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Cora (neural)"
    DAVIS_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Davis (neural)"
    ELIZABETH_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Elizabeth (neural)"
    EMMA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Emma (neural)"
    ERIC_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Eric (neural)"
    GUY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Guy (neural)"
    JACOB_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jacob (neural)"
    JANE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jane (neural)"
    JASON_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jason (neural)"
    JENNY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jenny (neural)"
    MICHELLE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Michelle (neural)"
    MONICA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Monica (neural)"
    NANCY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Nancy (neural)"
    ROGER_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Roger (neural)"
    SARA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Sara (neural)"
    STEFFAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Steffan (neural)"
    TONY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Tony (neural)"
    ANNETTE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Annette (neural)"
    CARLY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Carly (neural)"
    DARREN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Darren (neural)"
    DUNCAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Duncan (neural)"
    ELSIE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Elsie (neural)"
    FREYA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Freya (neural)"
    JOANNE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Joanne (neural)"
    KEN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ken (neural)"
    KIM_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Kim (neural)"
    NATASHA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Natasha (neural)"
    NEIL_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Neil (neural)"
    TIM_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Tim (neural)"
    TINA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Tina (neural)"
    WILLIAM_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "William (neural)"
    ABBI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Abbi (neural)"
    ALFIE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Alfie (neural)"
    BELLA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Bella (neural)"
    ELLIOT_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Elliot (neural)"
    ETHAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ethan (neural)"
    HOLLIE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Hollie (neural)"
    LIBBY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Libby (neural)"
    NOAH_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Noah (neural)"
    OLIVER_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Oliver (neural)"
    OLIVIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Olivia (neural)"
    RYAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ryan (neural)"
    SONIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Sonia (neural)"
    THOMAS_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Thomas (neural)"
    CLARA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Clara (neural)"
    LIAM_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Liam (neural)"
    NEERJA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Neerja (neural)"
    PRABHAT_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Prabhat (neural)"
    CONNOR_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Connor (neural)"
    EMILY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Emily (neural)"
    ANGELO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Angelo (neural)"
    BLESSICA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Blessica (neural)"
    HARRI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Harri (neural)"
    NOORA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Noora (neural)"
    SELMA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Selma (neural)"
    ALAIN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Alain (neural)"
    BRIGITTE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Brigitte (neural)"
    CELESTE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Celeste (neural)"
    CLAUDE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Claude (neural)"
    CORALIE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Coralie (neural)"
    DENISE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Denise (neural)"
    HENRI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Henri (neural)"
    JACQUELINE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jacqueline (neural)"
    JEROME_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jerome (neural)"
    JOSEPHINE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Josephine (neural)"
    MAURICE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Maurice (neural)"
    VIVIENNE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Vivienne (neural)"
    YVES_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yves (neural)"
    YVETTE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yvette (neural)"
    ANTOINE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Antoine (neural)"
    JEAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jean (neural)"
    SYLVIE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Sylvie (neural)"
    THIERRY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Thierry (neural)"
    ARIANE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ariane (neural)"
    FABRICE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Fabrice (neural)"
    AMALA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Amala (neural)"
    BERND_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Bernd (neural)"
    CHRISTOPH_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Christoph (neural)"
    CONRAD_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Conrad (neural)"
    ELKE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Elke (neural)"
    KASPER_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Kasper (neural)"
    KATJA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Katja (neural)"
    KILLIAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Killian (neural)"
    KLARISSA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Klarissa (neural)"
    KLAUS_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Klaus (neural)"
    LOUISA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Louisa (neural)"
    MAJA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Maja (neural)"
    RALF_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ralf (neural)"
    SERAPHINA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Seraphina (neural)"
    TANJA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Tanja (neural)"
    INGRID_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ingrid (neural)"
    JONAS_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jonas (neural)"
    JAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jan (neural)"
    LENI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Leni (neural)"
    ATHINA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Athina (neural)"
    NESTORAS_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Nestoras (neural)"
    DHWANI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Dhwani (neural)"
    NIRANJAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Niranjan (neural)"
    AVRI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Avri (neural)"
    HILA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Hila (neural)"
    MADHUR_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Madhur (neural)"
    SWARA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Swara (neural)"
    NOEMI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Noemi (neural)"
    TAMAS_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Tamas (neural)"
    GUDRUN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Gudrun (neural)"
    GUNNAR_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Gunnar (neural)"
    ARDI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ardi (neural)"
    GADIS_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Gadis (neural)"
    BENIGNO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Benigno (neural)"
    CALIMERO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Calimero (neural)"
    CATALDO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Cataldo (neural)"
    DIEGO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Diego (neural)"
    ELSA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Elsa (neural)"
    FABIOLA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Fabiola (neural)"
    FIAMMA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Fiamma (neural)"
    GIANNI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Gianni (neural)"
    GIUSEPPE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Giuseppe (neural)"
    IMELDA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Imelda (neural)"
    IRMA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Irma (neural)"
    ISABELLA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Isabella (neural)"
    LISANDRO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Lisandro (neural)"
    PALMIRA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Palmira (neural)"
    PIERINA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Pierina (neural)"
    RINALDO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Rinaldo (neural)"
    AOI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Aoi (neural)"
    DAICHI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Daichi (neural)"
    KEITA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Keita (neural)"
    MAYU_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Mayu (neural)"
    NANAMI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Nanami (neural)"
    NAOKI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Naoki (neural)"
    SHIORI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Shiori (neural)"
    GAGAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Gagan (neural)"
    SAPNA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Sapna (neural)"
    BONG_JIN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "BongJin (neural)"
    GOOK_MIN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "GookMin (neural)"
    HYUNSU_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Hyunsu (neural)"
    IN_JOON_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "InJoon (neural)"
    JI_MIN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "JiMin (neural)"
    SEO_HYEON_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "SeoHyeon (neural)"
    SOON_BOK_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "SoonBok (neural)"
    SUN_HI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "SunHi (neural)"
    YU_JIN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "YuJin (neural)"
    OSMAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Osman (neural)"
    YASMIN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yasmin (neural)"
    MIDHUN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Midhun (neural)"
    SOBHANA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Sobhana (neural)"
    FINN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Finn (neural)"
    ISELIN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Iselin (neural)"
    PERNILLE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Pernille (neural)"
    AGNIESZKA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Agnieszka (neural)"
    MAREK_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Marek (neural)"
    ZOFIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Zofia (neural)"
    DUARTE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Duarte (neural)"
    FERNANDA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Fernanda (neural)"
    RAQUEL_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Raquel (neural)"
    ANTONIO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Antonio (neural)"
    BRENDA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Brenda (neural)"
    DONATO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Donato (neural)"
    ELZA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Elza (neural)"
    FABIO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Fabio (neural)"
    FRANCISCA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Francisca (neural)"
    GIOVANNA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Giovanna (neural)"
    HUMBERTO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Humberto (neural)"
    JULIO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Julio (neural)"
    LEILA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Leila (neural)"
    LETICIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Leticia (neural)"
    MANUELA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Manuela (neural)"
    NICOLAU_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Nicolau (neural)"
    THALITA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Thalita (neural)"
    VALERIO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Valerio (neural)"
    YARA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yara (neural)"
    ALINA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Alina (neural)"
    EMIL_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Emil (neural)"
    DARIYA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Dariya (neural)"
    DMITRY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Dmitry (neural)"
    SVETLANA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Svetlana (neural)"
    LUKAS_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Lukas (neural)"
    VIKTORIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Viktoria (neural)"
    PETRA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Petra (neural)"
    ROK_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Rok (neural)"
    ABRIL_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Abril (neural)"
    ALONSO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Alonso (neural)"
    ALVARO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Alvaro (neural)"
    ARNAU_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Arnau (neural)"
    DARIO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Dario (neural)"
    ELIAS_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Elias (neural)"
    ELVIRA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Elvira (neural)"
    ESTRELLA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Estrella (neural)"
    IRENE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Irene (neural)"
    LAIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Laia (neural)"
    LIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Lia (neural)"
    NIL_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Nil (neural)"
    PALOMA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Paloma (neural)"
    SAUL_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Saul (neural)"
    TEO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Teo (neural)"
    TRIANA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Triana (neural)"
    VERA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Vera (neural)"
    XIMENA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ximena (neural)"
    BEATRIZ_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Beatriz (neural)"
    CANDELA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Candela (neural)"
    CARLOTA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Carlota (neural)"
    CECILIO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Cecilio (neural)"
    DALIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Dalia (neural)"
    GERARDO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Gerardo (neural)"
    JORGE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jorge (neural)"
    LARISSA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Larissa (neural)"
    LIBERTO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Liberto (neural)"
    LUCIANO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Luciano (neural)"
    MARINA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Marina (neural)"
    NURIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Nuria (neural)"
    PELAYO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Pelayo (neural)"
    RENATA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Renata (neural)"
    YAGO_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Yago (neural)"
    HILLEVI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Hillevi (neural)"
    MATTIAS_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Mattias (neural)"
    SOFIE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Sofie (neural)"
    PALLAVI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Pallavi (neural)"
    VALLUVAR_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Valluvar (neural)"
    MOHAN_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Mohan (neural)"
    SHRUTI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Shruti (neural)"
    ACHARA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Achara (neural)"
    NIWAT_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Niwat (neural)"
    PREMWADEE_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Premwadee (neural)"
    AHMET_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ahmet (neural)"
    EMEL_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Emel (neural)"
    OSTAP_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Ostap (neural)"
    POLINA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Polina (neural)"
    HOAI_MY_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "HoaiMy (neural)"
    NAM_MINH_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "NamMinh (neural)"
    ALED_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Aled (neural)"
    NIA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Nia (neural)"
    MOUNA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Mouna (neural)"
    JAMAL_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Jamal (neural)"
    UZMA_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Uzma (neural)"
    ASAD_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Asad (neural)"
    AAROHI_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Aarohi (neural)"
    MANOHAR_LEFT_PARENTHESIS_NEURAL_RIGHT_PARENTHESIS = "Manohar (neural)"

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CallVoice from a JSON string"""
        return cls(json.loads(json_str))
