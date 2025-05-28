"""
Tests para el módulo de respuestas
=================================

Tests unitarios para verificar la detección de patrones
y generación de respuestas apropiadas.

Autor: llopgui (https://github.com/llopgui/)
Licencia: CC BY-NC-SA 4.0
"""

import sys
from pathlib import Path

# Agregar src al path para imports en tests
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Imports deben estar después de la configuración del path
try:
    import pytest

    from bot.responses import (
        detect_pluto_planet_claim,
        get_pluto_fact,
        get_response,
        get_response_category,
    )
except ImportError as e:
    print(f"Error de importación: {e}")
    print("Asegúrate de que las dependencias estén instaladas")
    sys.exit(1)


class TestPlutoDetection:
    """Tests para la detección de afirmaciones sobre Plutón."""

    def test_detect_direct_claims(self) -> None:
        """Test detección de afirmaciones directas."""
        test_cases: list[str] = [
            "Plutón es un planeta",
            "pluton es un planeta",
            "pluto es un planeta",
            "Creo que Plutón es un planeta",
            "Para mí Plutón sigue siendo un planeta",
        ]

        for case in test_cases:
            assert detect_pluto_planet_claim(case), f"Failed: {case}"

    def test_detect_planet_lists(self) -> None:
        """Test detección en listas de planetas."""
        test_cases: list[str] = [
            "Los nueve planetas del sistema solar",
            (
                "Mercurio Venus Tierra Marte Júpiter Saturno Urano "
                "Neptuno Plutón"
            ),
            "Hay 9 planetas en total",
        ]

        for case in test_cases:
            assert detect_pluto_planet_claim(case), f"Failed: {case}"

    def test_detect_nostalgic_expressions(self) -> None:
        """Test detección de expresiones nostálgicas."""
        test_cases: list[str] = [
            "Extraño cuando Plutón era planeta",
            "Deberían devolver a Plutón su estatus de planeta",
            "Plutón debería ser planeta otra vez",
        ]

        for case in test_cases:
            assert detect_pluto_planet_claim(case), f"Failed: {case}"

    def test_no_false_positives(self) -> None:
        """Test que no detecte falsos positivos."""
        test_cases: list[str] = [
            "Plutón es un planeta enano",
            "Hola, ¿cómo estás?",
            "Me gusta la astronomía",
            "Plutón es muy frío",
            "Los planetas del sistema solar",
        ]

        for case in test_cases:
            assert not detect_pluto_planet_claim(
                case
            ), f"False positive: {case}"


class TestResponseGeneration:
    """Tests para la generación de respuestas."""

    def test_get_response_not_empty(self) -> None:
        """Test que las respuestas no estén vacías."""
        test_inputs: list[str] = [
            "Plutón es un planeta",
            "Hola bot",
            "Adiós",
            "Mensaje random",
        ]

        for input_text in test_inputs:
            response: str = get_response(input_text)
            assert response, f"Empty response for: {input_text}"
            assert len(response) > 0, f"Empty response for: {input_text}"

    def test_response_categories(self) -> None:
        """Test que las categorías se asignen correctamente."""
        test_cases: list[tuple[str, str]] = [
            ("Hola", "saludos"),
            ("Adiós", "despedidas"),
            # Para claims de Plutón, puede ser cualquier categoría válida
            ("Plutón es un planeta", "correcciones_cientificas"),
        ]

        for input_text, expected_category in test_cases:
            category: str = get_response_category(input_text)
            if expected_category == "correcciones_cientificas":
                # Para claims de Plutón, verificar categorías válidas
                valid_categories: list[str] = [
                    "correcciones_cientificas",
                    "respuestas_educativas",
                    "respuestas_sarcasticas",
                    "respuestas_humor",
                    "respuestas_comprensivas",
                ]
                assert (
                    category in valid_categories
                ), f"Unexpected category: {category}"
            else:
                assert (
                    category == expected_category
                ), f"Expected {expected_category}, got {category}"

    def test_empty_input(self) -> None:
        """Test comportamiento con entrada vacía."""
        response: str = get_response("")
        assert response
        assert "silencioso" in response.lower()


class TestPlutoFacts:
    """Tests para los datos de Plutón."""

    def test_get_pluto_fact_not_empty(self) -> None:
        """Test que los datos no estén vacíos."""
        fact: str = get_pluto_fact()
        assert fact
        assert len(fact) > 10  # Debe ser un texto sustancial

    def test_pluto_fact_consistency(self) -> None:
        """Test que los datos sean consistentes."""
        facts: set[str] = {get_pluto_fact() for _ in range(20)}
        assert len(facts) >= 3, "Debe haber al menos 3 datos diferentes"

    def test_pluto_fact_format(self) -> None:
        """Test que los datos tengan formato apropiado."""
        fact: str = get_pluto_fact()
        assert "**Dato" in fact, "Debe contener formato de dato"
        expected_emojis: list[str] = ["🧊", "⏰", "💕", "🏔️", "🌡️", "👥"]
        assert any(
            emoji in fact for emoji in expected_emojis
        ), "Debe contener emoji"


if __name__ == "__main__":
    pytest.main([__file__])
