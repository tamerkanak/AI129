import google.generativeai as genai
import os
from typing import Dict, List, Optional
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

class AIService:
    def __init__(self):
        # API anahtarını .env dosyasından al
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            print("UYARI: GOOGLE_API_KEY environment variable bulunamadı!")
            print("Vaka oluşturma özelliği sınırlı olacak.")
            # Geçici test anahtarı (gerçek uygulamada kullanmayın)
            api_key = 'AIzaSyByPqJtNQlHcldml-ArPHkYrJKkfFtX4es'
        
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-2.0-flash-lite')
            print("AI servisi başarıyla başlatıldı.")
        except Exception as e:
            print(f"AI servisi başlatma hatası: {str(e)}")
            self.model = None
    
    def generate_case(self, difficulty: str = 'medium', specialty: str = 'general') -> Dict:
        """Dinamik vaka oluşturucu"""
        prompt = f"""
        Tıp öğrencileri için {difficulty} seviyesinde bir {specialty} vaka senaryosu oluştur.
        
        SADECE aşağıdaki JSON formatında döndür, başka hiçbir şey yazma:
        {{
            "title": "Vaka başlığı",
            "patient_name": "Hasta adı",
            "age": yaş,
            "complaint": "Ana şikayet",
            "medical_history": "Tıbbi geçmiş",
            "symptoms": "Belirtiler",
            "questions": [
                {{"question": "Soru metni", "answer": "Kısa cevap", "type": "general"}},
                {{"question": "Soru metni", "answer": "Kısa cevap", "type": "physical_exam"}},
                {{"question": "Soru metni", "answer": "Kısa cevap", "type": "general"}},
                {{"question": "Soru metni", "answer": "Kısa cevap", "type": "physical_exam"}},
                {{"question": "Soru metni", "answer": "Kısa cevap", "type": "general"}}
            ]
        }}
        
        ÖNEMLİ: 
        - Sadece JSON döndür, açıklama yazma
        - Yaş sayı olmalı (örn: 45)
        - Cevaplar kısa olmalı (1-2 cümle)
        - Vaka gerçekçi ve eğitici olmalı
        """
        
        # Model kontrolü
        if not self.model:
            print("AI modeli mevcut değil, fallback case kullanılıyor.")
            return self._get_fallback_case()
        
        try:
            response = self.model.generate_content(prompt)
            import json
            import re
            
            # JSON'u temizle ve parse et
            text = response.text.strip()
            print(f"AI yanıtı: {text[:200]}...")  # Debug için
            
            # JSON bloğunu bul
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                case_data = json.loads(json_str)
                
                # Gerekli alanları kontrol et
                required_fields = ['title', 'patient_name', 'age', 'complaint', 'questions']
                if all(field in case_data for field in required_fields):
                    print("Vaka başarıyla oluşturuldu!")
                    return case_data
            
            # JSON parse edilemezse fallback
            print(f"JSON parse hatası: {text}")
            return self._get_fallback_case()
            
        except Exception as e:
            print(f"Vaka oluşturma hatası: {str(e)}")
            return self._get_fallback_case()
    
    def evaluate_solution(self, case_info: Dict, diagnosis: str, treatment: str) -> Dict:
        """Vaka çözümünü değerlendir"""
        # Model kontrolü
        if not self.model:
            return {
                "score": 75,
                "feedback": "AI servisi mevcut değil, standart değerlendirme yapılıyor.",
                "strengths": ["Çözüm sunulmuş"],
                "improvements": ["Daha detaylı analiz gerekli"]
            }
        
        prompt = f"""
        Tıp öğrencisinin vaka çözümünü değerlendir:
        
        VAKA BİLGİLERİ:
        Hasta: {case_info.get('patient_name', '')}
        Yaş: {case_info.get('age', '')}
        Şikayet: {case_info.get('complaint', '')}
        Tıbbi Geçmiş: {case_info.get('medical_history', '')}
        Belirtiler: {case_info.get('symptoms', '')}
        
        ÖĞRENCİ ÇÖZÜMÜ:
        Tanı: {diagnosis}
        Tedavi: {treatment}
        
        SADECE aşağıdaki JSON formatında döndür:
        {{
            "score": puan,
            "feedback": "Detaylı geri bildirim",
            "strengths": ["Güçlü yanlar"],
            "improvements": ["Geliştirilebilir alanlar"]
        }}
        """
        
        try:
            response = self.model.generate_content(prompt)
            import json
            import re
            
            text = response.text.strip()
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                return json.loads(json_str)
            
            return {
                "score": 75,
                "feedback": "Değerlendirme sırasında teknik bir hata oluştu.",
                "strengths": ["Çözüm sunulmuş"],
                "improvements": ["Daha detaylı analiz gerekli"]
            }
        except Exception as e:
            print(f"Değerlendirme hatası: {str(e)}")
            return {
                "score": 75,
                "feedback": "Değerlendirme sırasında teknik bir hata oluştu.",
                "strengths": ["Çözüm sunulmuş"],
                "improvements": ["Daha detaylı analiz gerekli"]
            }
    
    def generate_dynamic_answer(self, question: str, case_context: str) -> str:
        """Dinamik cevap üretimi"""
        # Model kontrolü
        if not self.model:
            return "Üzgünüm, şu anda cevap veremiyorum."
        
        prompt = f"""
        Tıp öğrencisinin sorduğu soruya hasta perspektifinden kısa ve öz cevap ver:
        
        VAKA BAĞLAMI: {case_context}
        SORU: {question}
        
        ÖNEMLİ: Sadece 1-2 kısa cümle ile cevap ver. Hasta gibi samimi ama kısa konuş.
        Örnek: "Dün gece yarısı başladı." veya "Evet, çok şiddetli ağrı var."
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Soru cevaplama hatası: {str(e)}")
            return "Üzgünüm, şu anda cevap veremiyorum."
    
    def _get_fallback_case(self) -> Dict:
        """API hatası durumunda kullanılacak örnek vaka"""
        return {
            "title": "Baş Ağrısı Vakası",
            "patient_name": "Ayşe Kaya",
            "age": 28,
            "complaint": "Şiddetli baş ağrısı ve bulantı",
            "medical_history": "Migren geçmişi var",
            "symptoms": "Baş ağrısı, bulantı, ışığa hassasiyet",
            "questions": [
                {"question": "Ağrı ne zaman başladı?", "answer": "Dün sabah uyandığımda.", "type": "general"},
                {"question": "Ağrının yeri neresi?", "answer": "Sağ şakak bölgesi.", "type": "general"},
                {"question": "Daha önce böyle ağrı yaşadınız mı?", "answer": "Evet, migren ataklarım oluyor.", "type": "general"},
                {"question": "Ateşiniz var mı?", "answer": "Hayır.", "type": "physical_exam"},
                {"question": "Boyun sertliği var mı?", "answer": "Hayır.", "type": "physical_exam"}
            ]
        }

# Global AI servis instance'ı
ai_service = AIService() 